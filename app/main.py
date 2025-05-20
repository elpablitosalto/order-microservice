from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

from .worker import process_order

app = FastAPI(
    title="Order Processing Microservice",
    description="A microservice for handling order processing with async task queue",
    version="1.0.0"
)

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class Order(BaseModel):
    customer_id: str
    items: List[OrderItem]
    shipping_address: str
    total_amount: float

class OrderResponse(BaseModel):
    order_id: str
    status: str
    created_at: datetime
    customer_id: str
    total_amount: float

@app.post("/orders/", response_model=OrderResponse)
async def create_order(order: Order):
    order_id = str(uuid.uuid4())
    
    # Create order response
    order_response = OrderResponse(
        order_id=order_id,
        status="pending",
        created_at=datetime.utcnow(),
        customer_id=order.customer_id,
        total_amount=order.total_amount
    )
    
    # Send order to Celery for processing
    process_order.delay(order_id, order.dict())
    
    return order_response

@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str):
    # In a real application, this would fetch from a database
    # For now, we'll return a mock response
    return OrderResponse(
        order_id=order_id,
        status="processing",
        created_at=datetime.utcnow(),
        customer_id="customer123",
        total_amount=100.00
    ) 