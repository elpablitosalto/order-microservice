from celery import Celery
import os
import time

# Initialize Celery
celery_app = Celery(
    'order_processor',
    broker=os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    backend=os.getenv('REDIS_URL', 'redis://localhost:6379/0')
)

@celery_app.task(name='process_order')
def process_order(order_id: str, order_data: dict):
    """
    Process an order asynchronously.
    In a real application, this would:
    1. Validate the order
    2. Process payment
    3. Update inventory
    4. Send notifications
    5. Update order status
    """
    # Simulate some processing time
    time.sleep(5)
    
    # In a real application, you would:
    # - Update the order status in the database
    # - Send notifications
    # - Handle payment processing
    # - Update inventory
    
    return {
        'order_id': order_id,
        'status': 'processed',
        'message': 'Order processed successfully'
    } 