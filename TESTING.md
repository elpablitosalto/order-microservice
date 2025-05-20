# Руководство по тестированию Order Processing Microservice

## Подготовка к тестированию

1. Установите зависимости для тестирования:
```bash
pip install -r requirements.txt
```

2. Убедитесь, что Redis запущен:
```bash
docker-compose up redis
```

## Запуск тестов

### Запуск всех тестов
```bash
pytest
```

### Запуск конкретного теста
```bash
pytest tests/test_api.py
pytest tests/test_worker.py
```

### Запуск теста с подробным выводом
```bash
pytest -v
```

### Запуск теста с выводом print-сообщений
```bash
pytest -s
```

## Структура тестов

### API тесты (tests/test_api.py)
- `test_create_order()`: Проверяет создание нового заказа
- `test_get_order()`: Проверяет получение информации о заказе
- `test_invalid_order_data()`: Проверяет обработку некорректных данных
- `test_nonexistent_order()`: Проверяет обработку несуществующего заказа

### Worker тесты (tests/test_worker.py)
- `test_process_order()`: Проверяет обработку заказа воркером
- `test_process_order_with_empty_data()`: Проверяет обработку заказа с пустыми данными

## Ручное тестирование API

### Создание заказа
```bash
curl -X POST "http://localhost:8000/orders/" \
     -H "Content-Type: application/json" \
     -d '{
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
         }'
```

### Получение информации о заказе
```bash
curl "http://localhost:8000/orders/{order_id}"
```

## Проверка Celery Worker

1. Запустите Celery worker:
```bash
celery -A app.worker worker --loglevel=info
```

2. Отправьте тестовый заказ через API
3. Проверьте логи Celery worker для подтверждения обработки заказа

## Проверка Redis

1. Подключитесь к Redis CLI:
```bash
docker exec -it order-microservice_redis_1 redis-cli
```

2. Проверьте очереди:
```bash
KEYS *
```

## Отладка

### Логи FastAPI
```bash
docker-compose logs web
```

### Логи Celery Worker
```bash
docker-compose logs celery_worker
```

### Логи Redis
```bash
docker-compose logs redis
```

## Рекомендации по тестированию

1. Всегда запускайте тесты в изолированной среде
2. Проверяйте как успешные сценарии, так и обработку ошибок
3. Тестируйте граничные случаи и некорректные данные
4. Используйте фикстуры pytest для подготовки тестовых данных
5. Следите за временем выполнения тестов
6. Проверяйте логи на наличие ошибок и предупреждений 