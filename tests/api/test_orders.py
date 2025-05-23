import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    """Test order creation endpoint"""
    order_data = {
        "customer_id": "test_customer_123",
        "shipping_address": "123 Test St",
        "items": [
            {
                "product_id": "test_product_123",
                "quantity": 2,
                "price": 29.99
            }
        ]
    }
    
    response = client.post("/api/v1/orders/", json=order_data)
    assert response.status_code == 201
    data = response.json()
    assert data["customer_id"] == order_data["customer_id"]
    assert data["shipping_address"] == order_data["shipping_address"]
    assert len(data["items"]) == 1
    assert data["items"][0]["product_id"] == order_data["items"][0]["product_id"]

def test_get_order():
    """Test getting order by ID"""
    # First create an order
    order_data = {
        "customer_id": "test_customer_123",
        "shipping_address": "123 Test St",
        "items": [
            {
                "product_id": "test_product_123",
                "quantity": 2,
                "price": 29.99
            }
        ]
    }
    
    create_response = client.post("/api/v1/orders/", json=order_data)
    order_id = create_response.json()["id"]
    
    # Then get the order
    response = client.get(f"/api/v1/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id
    assert data["customer_id"] == order_data["customer_id"] 