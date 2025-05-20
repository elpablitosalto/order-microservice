# Order Processing Microservice

A scalable microservice for handling order processing using FastAPI, Celery, and Redis.

## Features

- Asynchronous order processing using Celery
- RESTful API with FastAPI
- Redis for message queue
- Docker containerization
- OpenAPI documentation

## Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/order-microservice.git
cd order-microservice
```

2. Start the services using Docker Compose:
```bash
docker-compose up --build
```

The service will be available at http://localhost:8000

## API Documentation

Once the service is running, you can access the OpenAPI documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Create Order
- **POST** `/orders/`
- Creates a new order and processes it asynchronously

### Get Order Status
- **GET** `/orders/{order_id}`
- Retrieves the status of a specific order

## Development

For local development:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Redis:
```bash
docker-compose up redis
```

4. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

5. Start the Celery worker:
```bash
celery -A app.worker worker --loglevel=info
```

## License

MIT 