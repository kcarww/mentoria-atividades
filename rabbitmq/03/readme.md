# Customer Services - Passo a Passo com Antes e Depois

Este documento lista o que precisa ser mudado no projeto para ele funcionar de ponta a ponta, mas sem aplicar nenhuma alteracao no codigo ainda.

Objetivo final do sistema:

1. cadastrar cliente via API
2. publicar evento no RabbitMQ
3. consumir o evento em um worker
4. registrar o resultado em `NotificationLog`
5. validar tudo com testes

## 1. Resumo do que falta

Hoje o projeto ainda tem estes pontos em aberto:

- serializer de `NotificationLog` esta incorreto
- publicacao no RabbitMQ usa configuracao inconsistente
- `CustomerViewSet` nao trata falha ao publicar mensagem
- nao existe worker/consumer implementado
- nao existem testes cobrindo o fluxo principal
- nao existe arquivo de dependencias do projeto

## 2. Ordem recomendada

Para evitar retrabalho, a melhor sequencia e:

1. criar dependencias e ambiente
2. corrigir configuracao do RabbitMQ
3. corrigir serializer de `NotificationLog`
4. revisar `CustomerViewSet`
5. ajustar `messaging/rabbitmq.py`
6. implementar worker
7. adicionar testes
8. executar o fluxo completo

## 3. Dependencias do projeto

### O que esta faltando

O projeto nao possui `requirements.txt`, `pyproject.toml`, `Pipfile` ou equivalente.

### O que eu mudaria

Criaria um `requirements.txt` inicial com:

```txt
django
djangorestframework
pika
psycopg[binary]
```

Se voce for usar SQLite localmente no inicio, `psycopg[binary]` pode ficar para uma etapa posterior.

### Como ficaria

Arquivo novo:

```txt
django
djangorestframework
pika
psycopg[binary]
```

## 4. Corrigir configuracao do RabbitMQ em `core/settings.py`

### Problema

O publisher usa `settings.RABBITMQ_HOST`, mas o settings atual expoe `RABBITMQ_URL`.

### Antes

Trecho atual de [core/settings.py](/home/carlos/customer_services/core/settings.py):

```python
STATIC_URL = 'static/'
RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')
RABBITMQ_EXCHANGE = 'customer_services'
RABBITMQ_QUEUE = 'customer_services_queue'
RABBITMQ_ROUTING_KEY = 'customer.created'
```

### Depois

Eu manteria essa ideia e faria o publisher usar `RABBITMQ_URL` corretamente:

```python
STATIC_URL = 'static/'

RABBITMQ_URL = os.getenv(
    'RABBITMQ_URL',
    'amqp://guest:guest@localhost:5672/'
)
RABBITMQ_EXCHANGE = 'customer_services'
RABBITMQ_QUEUE = 'customer_services_queue'
RABBITMQ_ROUTING_KEY = 'customer.created'
```

### Observacao

Esse arquivo ja esta melhor do que na revisao inicial. O ponto pendente agora esta mais concentrado em `messaging/rabbitmq.py`, que ainda tenta ler `RABBITMQ_HOST`.

## 5. Corrigir `NotificationLogSerializer`

### Problema

O serializer foi declarado com a classe errada.

### Antes

Trecho atual de [customers/serializers.py](/home/carlos/customer_services/customers/serializers.py):

```python
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']

class NotificationLogSerializer(serializers.Serializer):
    class Meta:
        fields = ["id", "customer", "type", "status", "payload", "created_at"]
        read_only_fields = ['id', 'created_at']
```

### Depois

Eu mudaria para `ModelSerializer` e importaria `NotificationLog`:

```python
from rest_framework import serializers
from .models import Customer, NotificationLog


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']


class NotificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationLog
        fields = ['id', 'customer', 'type', 'status', 'payload', 'created_at']
        read_only_fields = ['id', 'created_at']
```

### Resultado esperado

O endpoint `notification-log` passa a serializar corretamente objetos do banco.

## 6. Revisar `CustomerViewSet`

### Problema

Hoje o cadastro salva o cliente e publica a mensagem, mas sem tratamento de erro.

### Antes

Trecho atual de [customers/views.py](/home/carlos/customer_services/customers/views.py):

```python
from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, NotificationLog
from .serializers import CustomerSerializer, NotificationLogSerializer
from messaging.rabbitmq import publish_message

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        customer = serializer.save()
        publish_message(customer.id, customer.email)


class NotificationLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NotificationLog.objects.all()
    serializer_class = NotificationLogSerializer
```

### Depois

Eu deixaria pelo menos com tratamento de falha e limparia imports nao usados:

```python
from rest_framework import viewsets
from rest_framework.exceptions import APIException

from messaging.rabbitmq import publish_message

from .models import Customer, NotificationLog
from .serializers import CustomerSerializer, NotificationLogSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        customer = serializer.save()
        published = publish_message(customer.id, customer.email)

        if not published:
            raise APIException('Nao foi possivel publicar o evento do cliente.')


class NotificationLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NotificationLog.objects.all()
    serializer_class = NotificationLogSerializer
```

### Alternativa

Se voce preferir nao falhar a API quando o RabbitMQ estiver fora, eu posso mudar esse comportamento para apenas registrar um erro e seguir.

## 7. Ajustar `messaging/rabbitmq.py`

### Problemas

- usa `settings.RABBITMQ_HOST`, mas esse valor nao existe
- nomes com typo
- nao trata excecoes
- nao retorna sucesso/falha

### Antes

Trecho atual de [messaging/rabbitmq.py](/home/carlos/customer_services/messaging/rabbitmq.py):

```python
import json
import pika
from django.conf import settings

def _conection():
    return pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))


def publish_message(customer_id, email):
    payload = {"event": "customer.created","customer_id": customer_id,"email": email}
    conn = _conection()
    
    chanel = conn.channel()
 
    chanel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)
    chanel.queue_bind(
        exchange=settings.RABBITMQ_EXCHANGE, 
        queue=settings.RABBITMQ_QUEUE, 
        routing_key=settings.RABBITMQ_ROUTING_KEY
    )

    chanel.basic_publish(
        exchange=settings.RABBITMQ_EXCHANGE,
        routing_key=settings.RABBITMQ_ROUTING_KEY,
        body=json.dumps(payload),
        properties=pika.BasicProperties(content_type="application/json", delivery_mode=2)
    )
    conn.close()
```

### Depois

Eu mudaria para usar `pika.URLParameters(settings.RABBITMQ_URL)` e retornaria `True` ou `False`:

```python
import json

import pika
from django.conf import settings


def _connection():
    parameters = pika.URLParameters(settings.RABBITMQ_URL)
    return pika.BlockingConnection(parameters)


def publish_message(customer_id, email):
    payload = {
        'event': 'customer.created',
        'customer_id': customer_id,
        'email': email,
    }

    connection = None

    try:
        connection = _connection()
        channel = connection.channel()

        channel.exchange_declare(
            exchange=settings.RABBITMQ_EXCHANGE,
            exchange_type='direct',
            durable=True,
        )
        channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)
        channel.queue_bind(
            exchange=settings.RABBITMQ_EXCHANGE,
            queue=settings.RABBITMQ_QUEUE,
            routing_key=settings.RABBITMQ_ROUTING_KEY,
        )
        channel.basic_publish(
            exchange=settings.RABBITMQ_EXCHANGE,
            routing_key=settings.RABBITMQ_ROUTING_KEY,
            body=json.dumps(payload),
            properties=pika.BasicProperties(
                content_type='application/json',
                delivery_mode=2,
            ),
        )
        return True
    except pika.exceptions.AMQPError:
        return False
    finally:
        if connection and connection.is_open:
            connection.close()
```

### Resultado esperado

A view passa a ter uma resposta clara sobre sucesso ou falha da publicacao.

## 8. Padronizar `NotificationLog.type`

### Problema

O model usa um valor textual mais solto para `type`.

### Antes

Trecho atual de [customers/models.py](/home/carlos/customer_services/customers/models.py):

```python
class NotificationLog(models.Model):
    STATUS_CHOICES = [('SENT', 'SENT'), ('FAILED', 'FAILED')]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, default='EMAIL BOAS VINDAS')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### Depois

Eu padronizaria para algo tecnico e previsivel:

```python
class NotificationLog(models.Model):
    STATUS_CHOICES = [('SENT', 'SENT'), ('FAILED', 'FAILED')]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, default='WELCOME_EMAIL')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### Observacao

Esse ponto e recomendacao de consistencia. Nao e o maior bloqueador de execucao.

## 9. Implementar o worker

### Problema

Os apps `messaging` e `workers` ainda nao implementam o consumidor.

### Antes

Arquivos como [workers/views.py](/home/carlos/customer_services/workers/views.py) e [workers/models.py](/home/carlos/customer_services/workers/models.py) estao apenas com scaffold.

```python
from django.shortcuts import render

# Create your views here.
```

### Depois

Em vez de colocar isso em `views.py`, eu criaria um command do Django, por exemplo:

`workers/management/commands/consume_customer_created.py`

Exemplo de estrutura:

```python
import json
import time

import pika
from django.conf import settings
from django.core.management.base import BaseCommand

from customers.models import Customer, NotificationLog


class Command(BaseCommand):
    help = 'Consume eventos customer.created'

    def handle(self, *args, **options):
        connection = self._connect_with_retry()
        self.stdout.write(self.style.SUCCESS('Conectado ao RabbitMQ com sucesso.'))
        channel = connection.channel()

        channel.exchange_declare(
            exchange=settings.RABBITMQ_EXCHANGE,
            exchange_type='direct',
            durable=True,
        )
        channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)
        channel.queue_bind(
            exchange=settings.RABBITMQ_EXCHANGE,
            queue=settings.RABBITMQ_QUEUE,
            routing_key=settings.RABBITMQ_ROUTING_KEY,
        )

        def callback(ch, method, properties, body):
            payload = json.loads(body)
            self.stdout.write(f'Mensagem recebida: {payload}')

            try:
                customer = Customer.objects.get(id=payload['customer_id'])

                NotificationLog.objects.create(
                    customer=customer,
                    type='WELCOME_EMAIL',
                    status='SENT',
                    payload=payload,
                )

                ch.basic_ack(delivery_tag=method.delivery_tag)
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Evento processado para customer_id={customer.id}.'
                    )
                )
            except Customer.DoesNotExist:
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
                self.stdout.write(
                    self.style.ERROR(
                        f"Cliente nao encontrado para customer_id={payload.get('customer_id')}."
                    )
                )
            except Exception as exc:
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
                self.stdout.write(
                    self.style.ERROR(f'Erro ao processar mensagem: {exc}')
                )

        channel.basic_consume(
            queue=settings.RABBITMQ_QUEUE,
            on_message_callback=callback,
        )
        self.stdout.write('Worker aguardando mensagens...')
        channel.start_consuming()

    def _connect_with_retry(self, retries=12, delay=5):
        parameters = pika.URLParameters(settings.RABBITMQ_URL)
        last_error = None

        for attempt in range(1, retries + 1):
            try:
                self.stdout.write(
                    f'Tentando conectar ao RabbitMQ ({attempt}/{retries})...'
                )
                return pika.BlockingConnection(parameters)
            except pika.exceptions.AMQPConnectionError as exc:
                last_error = exc
                self.stdout.write(
                    self.style.WARNING(
                        f'RabbitMQ indisponivel. Nova tentativa em {delay}s.'
                    )
                )
                time.sleep(delay)

        raise last_error
```

### Resultado esperado

Voce consegue subir um segundo processo para consumir as mensagens:

```bash
python3 manage.py consume_customer_created
```

## 10. Adicionar testes

### Problema

Os testes atuais estao vazios.

### Antes

Trecho atual de [customers/tests.py](/home/carlos/customer_services/customers/tests.py):

```python
from django.test import TestCase

# Create your tests here.
```

### Depois

Eu adicionaria pelo menos testes como estes:

```python
from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from customers.models import Customer


class CustomerAPITests(APITestCase):
    @patch('customers.views.publish_message', return_value=True)
    def test_create_customer(self, publish_message_mock):
        response = self.client.post(
            '/customer/',
            {'name': 'Carlos', 'email': 'carlos@example.com'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        publish_message_mock.assert_called_once()

    @patch('customers.views.publish_message', return_value=False)
    def test_create_customer_when_publish_fails(self, publish_message_mock):
        response = self.client.post(
            '/customer/',
            {'name': 'Carlos', 'email': 'carlos@example.com'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
```

### Resultado esperado

Voce passa a validar o comportamento da API sem depender de RabbitMQ real.

## 11. Fluxo final esperado

Depois dessas mudancas, o comportamento desejado e:

1. `POST /customer/`
2. API salva o cliente
3. API publica `customer.created`
4. worker consome a mensagem
5. worker grava `NotificationLog`
6. `GET /notification-log/` retorna o historico

## 12. Como executar depois das correcoes

### Ambiente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### RabbitMQ

```bash
docker run -d --hostname rabbit --name rabbitmq \
  -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

### Banco

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### API

```bash
python3 manage.py runserver
```

### Worker

```bash
python3 manage.py consume_customer_created
```

### Teste manual

```bash
curl -X POST http://127.0.0.1:8000/customer/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Carlos","email":"carlos@example.com"}'
```

```bash
curl http://127.0.0.1:8000/notification-log/
```

## 13. Checklist final

- criar `requirements.txt`
- corrigir serializer de `NotificationLog`
- revisar `CustomerViewSet`
- ajustar publisher do RabbitMQ
- implementar consumer
- padronizar `NotificationLog.type`
- criar testes
- rodar migrations
- subir API e worker
- validar criacao de cliente e consulta de logs

## 14. Proximo passo

Se voce quiser, eu posso fazer a proxima versao deste README ainda mais detalhada, separando em:

1. mudancas obrigatorias para funcionar
2. mudancas recomendadas para robustez
3. mudancas opcionais de limpeza

Ou, quando voce autorizar, eu implemento exatamente os pontos aprovados por voce.
