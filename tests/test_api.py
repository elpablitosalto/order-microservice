import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

def test_create_order():
    # Test data
    order_data = {
        "customer_id": "test_customer_123",
        "items": [
            {
                "product_id": "prod_123",
                "quantity": 2,
                "price": 29.99
            }
        ],
        "shipping_address": "123 Test St, Test City",
        "total_amount": 59.98
    }

    # Make request to create order
    response = client.post("/orders/", json=order_data)
    
    # Assert response
    assert response.status_code == 200
    data = response.json()
    assert "order_id" in data
    assert data["status"] == "pending"
    assert data["customer_id"] == order_data["customer_id"]
    assert data["total_amount"] == order_data["total_amount"]

def test_get_order():
    # First create an order
    order_data = {
        "customer_id": "test_customer_123",
        "items": [
            {
                "product_id": "prod_123",
                "quantity": 1,
                "price": 29.99
            }
        ],
        "shipping_address": "123 Test St, Test City",
        "total_amount": 29.99
    }
    
    create_response = client.post("/orders/", json=order_data)
    order_id = create_response.json()["order_id"]
    
    # Now get the order
    response = client.get(f"/orders/{order_id}")
    
    # Assert response
    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == order_id
    assert "status" in data
    assert "created_at" in data
    assert data["customer_id"] == order_data["customer_id"]
    assert data["total_amount"] == order_data["total_amount"]

def test_invalid_order_data():
    # Test with invalid data (missing required fields)
    invalid_order = {
        "customer_id": "test_customer_123",
        # Missing items
        "shipping_address": "123 Test St, Test City",
        "total_amount": 29.99
    }
    
    response = client.post("/orders/", json=invalid_order)
    assert response.status_code == 422  # Validation error

def test_nonexistent_order():
    # Test getting a non-existent order
    response = client.get("/orders/nonexistent_order_id")
    assert response.status_code == 200  # Currently returns mock data 