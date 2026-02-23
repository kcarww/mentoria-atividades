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
            print(f"[worker] RabbitMQ não está pronto (tentativa {attempt}/{max_retries})... esperando {delay}s")
            time.sleep(delay)

    raise RuntimeError("Não consegui conectar no RabbitMQ após várias tentativas.")

connection = connect_with_retry()
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

def callback(ch, method, properties, body):
    product = json.loads(body)
    print(f"[worker] Processando: {product}")
    time.sleep(3)
    print("[worker] Processado com sucesso!")

    # Se você quiser evoluir a aula, troque auto_ack=True por ack manual.
    # ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

print("[worker] Aguardando mensagens...")
channel.start_consuming()
