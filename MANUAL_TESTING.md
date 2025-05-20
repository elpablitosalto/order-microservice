# Пошаговая инструкция по тестированию Order Processing Microservice

## 1. Запуск сервисов

1. Откройте терминал и перейдите в директорию проекта:
```bash
cd order-microservice
```

2. Запустите все сервисы с помощью Docker Compose:
```bash
docker-compose up --build
```

3. Дождитесь, пока все сервисы запустятся. Вы должны увидеть сообщения о запуске:
   - FastAPI сервер на порту 8000
   - Celery worker
   - Redis

## 2. Тестирование API через Postman

### 2.1 Создание заказа

1. Откройте Postman
2. Создайте новый POST запрос:
   - URL: `http://localhost:8000/orders/`
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
    "shipping_address": "ул. Тестовая, 123, Москва",
    "total_amount": 109.97
}
```

3. Отправьте запрос
4. Ожидаемый результат:
   - Status: 200 OK
   - Response body должен содержать:
     - order_id (UUID)
     - status: "pending"
     - created_at (timestamp)
     - customer_id: "customer_123"
     - total_amount: 109.97

### 2.2 Получение информации о заказе

1. Скопируйте `order_id` из предыдущего ответа
2. Создайте новый GET запрос:
   - URL: `http://localhost:8000/orders/{order_id}` (замените {order_id} на скопированный ID)
   - Method: GET

3. Отправьте запрос
4. Ожидаемый результат:
   - Status: 200 OK
   - Response body должен содержать информацию о заказе

### 2.3 Тестирование обработки ошибок

1. Создайте новый POST запрос с некорректными данными:
   - URL: `http://localhost:8000/orders/`
   - Method: POST
   - Body (raw, JSON):
```json
{
    "customer_id": "customer_123",
    "shipping_address": "ул. Тестовая, 123, Москва",
    "total_amount": 100.00
}
```

2. Отправьте запрос
3. Ожидаемый результат:
   - Status: 422 Unprocessable Entity
   - Response body должен содержать описание ошибки валидации

## 3. Проверка Celery Worker

1. Откройте новый терминал
2. Выполните команду для просмотра логов Celery worker:
```bash
docker-compose logs -f celery_worker
```

3. В Postman отправьте новый заказ (как в шаге 2.1)
4. В логах Celery worker вы должны увидеть:
   - Получение задачи
   - Начало обработки заказа
   - Завершение обработки заказа

## 4. Проверка Redis

1. Откройте новый терминал
2. Подключитесь к Redis CLI:
```bash
docker exec -it order-microservice_redis_1 redis-cli
```

3. Проверьте очереди:
```bash
KEYS *
```

4. Вы должны увидеть ключи, связанные с Celery

## 5. Проверка документации API

1. Откройте в браузере:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

2. Проверьте:
   - Доступность всех эндпоинтов
   - Описание моделей данных
   - Примеры запросов

## 6. Остановка сервисов

1. В терминале, где запущен Docker Compose, нажмите Ctrl+C
2. Выполните команду:
```bash
docker-compose down
```

## Ожидаемые результаты тестирования

1. Все API запросы должны возвращать корректные ответы
2. Celery worker должен обрабатывать заказы асинхронно
3. Redis должен хранить очереди задач
4. Документация API должна быть доступна и содержать актуальную информацию
5. Обработка ошибок должна работать корректно

## Возможные проблемы и их решение

1. Если сервисы не запускаются:
   - Проверьте, что порты 8000 и 6379 свободны
   - Проверьте логи Docker Compose

2. Если Celery worker не обрабатывает задачи:
   - Проверьте подключение к Redis
   - Проверьте логи Celery worker

3. Если API возвращает ошибки:
   - Проверьте формат отправляемых данных
   - Проверьте логи FastAPI 