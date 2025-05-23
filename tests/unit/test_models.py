import pytest
from app.models import Order, OrderItem

def test_order_creation():
    """Test order creation with valid data"""
    order = Order(
        customer_id="test_customer_123",
        shipping_address="123 Test St",
        total_amount=100.00
    )
    assert order.customer_id == "test_customer_123"
    assert order.shipping_address == "123 Test St"
    assert order.total_amount == 100.00
    assert order.status == "pending"

def test_order_item_creation():
    """Test order item creation with valid data"""
    item = OrderItem(
        product_id="test_product_123",
        quantity=2,
        price=29.99
    )
    assert item.product_id == "test_product_123"
    assert item.quantity == 2
    assert item.price == 29.99
    assert item.total_price == 59.98 