# Step-by-Step Guide for Testing Order Processing Microservice

## 1. Starting Services

1. Open terminal and navigate to project directory:
```bash
cd order-microservice
```

2. Start all services using Docker Compose:
```bash
docker compose up --build
```

3. Wait until all services are started. You should see messages about:
   - FastAPI server on port 8000
   - Celery worker
   - Redis

## 2. Testing API via Postman

### 2.1 Creating an Order

1. Open Postman
2. Create a new POST request:
   - URL: `http://localhost:8080/orders/`
   - Method: POST
   - Headers: 
     - Key: `Content-Type`
     - Value: `application/json`
   - Body (raw, JSON):
```json
{
    "customer_id": "customer_123",
    "items": [
        {
            "product_id": "prod_1",
            "quantity": 2,
            "price": 29.99
        },
        {
            "product_id": "prod_2",
            "quantity": 1,
            "price": 49.99
        }
    ],
    "shipping_address": "123 Test St, Moscow",
    "total_amount": 109.97
}
```

3. Send the request
4. Expected result:
   - Status: 200 OK
   - Response body should contain:
     - order_id (UUID)
     - status: "pending"
     - created_at (timestamp)
     - customer_id: "customer_123"
     - total_amount: 109.97

### 2.2 Getting Order Information

1. Copy `order_id` from the previous response
2. Create a new GET request:
   - URL: `http://localhost:8080/orders/{order_id}` (replace {order_id} with the copied ID)
   - Method: GET

3. Send the request
4. Expected result:
   - Status: 200 OK
   - Response body should contain order information

### 2.3 Testing Error Handling

1. Create a new POST request with invalid data:
   - URL: `http://localhost:8000/orders/`
   - Method: POST
   - Body (raw, JSON):
```json
{
    "customer_id": "customer_123",
    "shipping_address": "123 Test St, Moscow",
    "total_amount": 100.00
}
```

2. Send the request
3. Expected result:
   - Status: 422 Unprocessable Entity
   - Response body should contain validation error description

## 3. Checking Celery Worker

1. Open a new terminal
2. Run command to view Celery worker logs:
```bash
docker compose logs -f celery_worker
```

3. Send a new order in Postman (as in step 2.1)
4. In Celery worker logs you should see:
   - Task received
   - Order processing started
   - Order processing completed

## 4. Checking Redis

1. Open a new terminal
2. Connect to Redis CLI:
```bash
docker exec -it order-microservice-redis-1 redis-cli
```

3. Check queues:
```bash
KEYS *
```

4. You should see keys related to Celery

## 5. Checking API Documentation

1. Open in browser:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

2. Check:
   - Availability of all endpoints
   - Data model descriptions
   - Request examples

## 6. Stopping Services

1. In the terminal where Docker Compose is running, press Ctrl+C
2. Run command:
```bash
docker compose down
```

## Expected Test Results

1. All API requests should return correct responses
2. Celery worker should process orders asynchronously
3. Redis should store task queues
4. API documentation should be available and contain up-to-date information
5. Error handling should work correctly

## Possible Issues and Solutions

1. If services don't start:
   - Check if ports 8000 and 6379 are free
   - Check Docker Compose logs

2. If Celery worker doesn't process tasks:
   - Check Redis connection
   - Check Celery worker logs

3. If API returns errors:
   - Check the format of sent data
   - Check FastAPI logs 