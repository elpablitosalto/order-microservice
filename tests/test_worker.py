import pytest
from app.worker import process_order
import time

def test_process_order():
    # Test data
    order_id = "test_order_123"
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
    
    # Call the task directly (not through Celery)
    result = process_order(order_id, order_data)
    
    # Assert the result
    assert result["order_id"] == order_id
    assert result["status"] == "processed"
    assert "message" in result
    assert result["message"] == "Order processed successfully"

def test_process_order_with_empty_data():
    # Test with empty order data
    order_id = "test_order_456"
    order_data = {}
    
    result = process_order(order_id, order_data)
    
    assert result["order_id"] == order_id
    assert result["status"] == "processed" 