import pika
import json
import time

RABBIT_HOST = "rabbitmq"
QUEUE_NAME = "products"

def connect_with_retry(max_retries=30, delay=2):
    for attempt in range(1, max_retries + 1):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST)
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print(f"[app] RabbitMQ não está pronto (tentativa {attempt}/{max_retries})... esperando {delay}s")
            time.sleep(delay)

    raise RuntimeError("Não consegui conectar no RabbitMQ após várias tentativas.")

connection = connect_with_retry()
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

product = {"codigo": "P001", "nome": "Notebook", "preco": 3500}

channel.basic_publish(
    exchange="",
    routing_key=QUEUE_NAME,
    body=json.dumps(product),
)

print("[app] Produto enviado para fila!")
connection.close()
