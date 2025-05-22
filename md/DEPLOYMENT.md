# Order Processing Microservice Deployment Guide

## 1. Server Preparation

1. Install Docker and Docker Compose:
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

## 2. DNS Configuration

1. Add an A record in your domain's DNS settings:
   - Name: `order-microservice`
   - Value: Your server's IP address
   - TTL: 3600 (or less)

## 3. Service Deployment

1. Copy all project files to the server:
```bash
scp -r ./* user@your-server:/path/to/order-microservice/
```

2. Navigate to the project directory:
```bash
cd /path/to/order-microservice
```

3. Start the services:
```bash
docker compose up -d --build
```

## 4. Service Verification

1. Check service availability:
```bash
curl http://localhost:8080/docs
```

2. Check logs:
```bash
docker compose logs -f
```

## 5. Service Update

To update the service, run:
```bash
git pull
docker compose down
docker compose up -d --build
```

## 6. Monitoring

1. Check container status:
```bash
docker compose ps
```

2. View logs:
```bash
docker compose logs -f [service_name]
```

## Possible Issues and Solutions

1. If service is unavailable:
   - Check DNS settings
   - Check firewall (port 8080 should be open)
   - Check Nginx logs: `docker compose logs nginx`

2. If Redis is unavailable:
   - Check Redis logs: `docker compose logs redis`
   - Check network settings in docker-compose.yml 