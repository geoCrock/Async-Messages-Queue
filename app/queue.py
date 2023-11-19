# // TODO: Написать очередь запросов для RabbitMQimport aio_pika
import pika

from config import RABBITMQ_URL, EXCHANGE_NAME

# Переменне из окружения для rabbitmq
RABBITMQ_URL = RABBITMQ_URL
EXCHANGE_NAME = EXCHANGE_NAME


def send_to_rabbit(message):
    message = str(message)
    # Соединение с сервером RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Объявление очереди
    channel.queue_declare(queue='hello')

    # Отправка сообщения
    channel.basic_publish(exchange='', routing_key='hello', body=message)

    print(f" [x] Sent '{message}'")

    # Закрытие соединения
    connection.close()
