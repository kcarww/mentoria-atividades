# Django + DRF + RabbitMQ (pika) + Postgres --- Projeto Completo

Este projeto demonstra:

-   Django REST Framework (CRUD)
-   RabbitMQ com pika (publisher + consumer)
-   Worker separado
-   Postgres no Docker
-   Execução local primeiro, depois containerizado
-   Solução para:
    -   Erro AMQPConnectionError
    -   Problemas de permissão (EACCES no WSL)

------------------------------------------------------------------------

# PARTE 1 --- Projeto Local (WSL)

## 1) Criar pasta e ambiente virtual

``` bash
mkdir -p ~/customer_events
cd ~/customer_events

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## 2) Instalar dependências

``` bash
pip install django djangorestframework pika python-dotenv
```

## 3) Criar projeto Django

``` bash
django-admin startproject core .
```

## 4) Criar apps

``` bash
python manage.py startapp customers
python manage.py startapp messaging
python manage.py startapp workers
```

------------------------------------------------------------------------

## 5) Configurar settings.py

Adicionar em INSTALLED_APPS:

``` python
"rest_framework",
"customers",
"messaging",
"workers",
```

Adicionar ao final:

``` python
import os
from urllib.parse import urlparse

RABBITMQ_URL = os.environ.get("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
RABBITMQ_EXCHANGE = "events"
RABBITMQ_QUEUE = "customer_events"
RABBITMQ_ROUTING_KEY = "customer.created"

DATABASE_URL = os.environ.get("DATABASE_URL", "")

if DATABASE_URL:
    db_url = urlparse(DATABASE_URL)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": db_url.path.lstrip("/"),
            "USER": db_url.username,
            "PASSWORD": db_url.password,
            "HOST": db_url.hostname,
            "PORT": db_url.port or 5432,
        }
    }
```

------------------------------------------------------------------------

## 6) Criar models

customers/models.py:

``` python
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class NotificationLog(models.Model):
    STATUS_CHOICES = [("SENT", "SENT"), ("FAILED", "FAILED")]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="notifications")
    type = models.CharField(max_length=50, default="WELCOME_EMAIL")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
```

Migrar:

``` bash
python manage.py makemigrations
python manage.py migrate
```

------------------------------------------------------------------------

## 7) Subir RabbitMQ local

``` bash
docker run -d --name rabbitmq   -p 5672:5672 -p 15672:15672   rabbitmq:3-management
```

------------------------------------------------------------------------

# PARTE 2 --- Containerização

## 8) requirements.txt

``` txt
asgiref==3.11.1
Django==6.0.2
djangorestframework==3.16.1
pika==1.3.2
python-dotenv==1.2.2
sqlparse==0.5.5
psycopg2-binary==2.9.11
```

------------------------------------------------------------------------

## 9) wait_for_rabbitmq.py

``` python
import os
import time
import pika

url = os.environ.get("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")
timeout = int(os.environ.get("RABBITMQ_WAIT_TIMEOUT", "60"))

start = time.time()
while True:
    try:
        conn = pika.BlockingConnection(pika.URLParameters(url))
        conn.close()
        print("RabbitMQ is ready!")
        break
    except Exception as e:
        if time.time() - start > timeout:
            raise SystemExit(f"RabbitMQ not ready after {timeout}s: {e}")
        print("Waiting for RabbitMQ...")
        time.sleep(2)
```

------------------------------------------------------------------------

## 10) Dockerfile

``` dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends   build-essential   && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
```

------------------------------------------------------------------------

## 11) .env

``` env
DJANGO_SETTINGS_MODULE=core.settings
DEBUG=1

DATABASE_URL=postgres://appuser:apppass@db:5432/appdb
RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/
RABBITMQ_WAIT_TIMEOUT=60
```

------------------------------------------------------------------------

## 12) docker-compose.yml

Descubra UID/GID:

``` bash
id -u
id -g
```

Use no campo user.

``` yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppass
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"
      - "15672:15672"

  api:
    build: .
    user: "1000:1000"
    env_file: .env
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
      - rabbitmq

  worker:
    build: .
    user: "1000:1000"
    env_file: .env
    command: sh -c "python wait_for_rabbitmq.py && python manage.py migrate && python manage.py consume_customer_events"
    volumes:
      - .:/app
    depends_on:
      - db
      - rabbitmq

volumes:
  pgdata:
```

------------------------------------------------------------------------

# 13) Subir projeto

``` bash
docker compose down -v
docker compose up --build
```

------------------------------------------------------------------------

# 14) Testar

``` bash
curl -X POST http://localhost:8000/api/customers/   -H "Content-Type: application/json"   -d '{"name":"Carlos","email":"carlos@docker.com"}'

curl http://localhost:8000/api/notification-logs/
```

RabbitMQ UI: http://localhost:15672 (guest/guest)

------------------------------------------------------------------------

# Problemas Resolvidos

✔ Permissão EACCES → usar user: "UID:GID" no compose\
✔ AMQPConnectionError → wait_for_rabbitmq.py\
✔ Worker subir antes do migrate → worker também roda migrate

------------------------------------------------------------------------

Projeto completo funcionando 🎉
