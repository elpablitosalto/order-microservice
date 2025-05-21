# Инструкция по развертыванию Order Processing Microservice

## 1. Подготовка сервера

1. Установите Docker и Docker Compose:
```bash
# Установка Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Установка Docker Compose
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

## 2. Настройка DNS

1. Добавьте A-запись в DNS-настройках вашего домена:
   - Имя: `order-microservice`
   - Значение: IP-адрес вашего сервера
   - TTL: 3600 (или меньше)

## 3. Развертывание сервиса

1. Скопируйте все файлы проекта на сервер:
```bash
scp -r ./* user@your-server:/path/to/order-microservice/
```

2. Перейдите в директорию проекта:
```bash
cd /path/to/order-microservice
```

3. Запустите сервисы:
```bash
docker compose up -d --build
```

## 4. Проверка работоспособности

1. Проверьте доступность сервиса:
```bash
curl http://order-microservice.pavel-khmelev-portfolio.webtm.ru/docs
```

2. Проверьте логи:
```bash
docker compose logs -f
```

## 5. Обновление сервиса

Для обновления сервиса выполните:
```bash
git pull
docker compose down
docker compose up -d --build
```

## 6. Мониторинг

1. Проверка статуса контейнеров:
```bash
docker compose ps
```

2. Просмотр логов:
```bash
docker compose logs -f [service_name]
```

## Возможные проблемы и их решение

1. Если сервис недоступен:
   - Проверьте DNS-настройки
   - Проверьте файрвол (порт 80 должен быть открыт)
   - Проверьте логи Nginx: `docker compose logs nginx`

2. Если Redis недоступен:
   - Проверьте логи Redis: `docker compose logs redis`
   - Проверьте сетевые настройки в docker-compose.yml 