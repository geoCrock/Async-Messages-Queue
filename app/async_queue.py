import aio_pika

from datetime import datetime
from app.db import SessionLocal, TextTable
from config import RABBITMQ_URL
from xcount import count_x


# Асинхронная функция для отправки сообщения
async def send_message(title, text):
    # Устанавливаем соединение с RabbitMQ
    connection = await aio_pika.connect_robust(RABBITMQ_URL)

    # Создаем канал для обмена данными с RabbitMQ
    channel = await connection.channel()

    # Задаем имя очереди
    queue_name = "text"

    # Объявляем очередь
    await channel.declare_queue(queue_name)

    # Создаем тело сообщения
    message_body = text

    # Создаем объект сообщения с указанным телом и хедом
    message = aio_pika.Message(body=message_body.encode(), headers={'title': f'{title}'})

    # Публикуем сообщение в очередь
    await channel.default_exchange.publish(message, routing_key=queue_name)

    # Выводим информацию о том, что сообщение отправлено
    print(f" [x] Sent '{message_body}'")

    # Закрываем соединение
    await connection.close()


async def receive_message():
    # Устанавливаем соединение с RabbitMQ
    connection = await aio_pika.connect_robust(RABBITMQ_URL)

    # Создаем канал для обмена данными с RabbitMQ
    channel = await connection.channel()

    # Задаем имя очереди
    queue_name = "text"

    # Объявляем очередь
    queue = await channel.declare_queue(queue_name)

    # Функция обратного вызова для обработки полученных сообщений
    async def callback(message: aio_pika.IncomingMessage):
        # Асинхронно обрабатываем сообщение
        async with message.process():
            # Выводим сообщение
            title = message.headers.get("title", "")
            x = await count_x(message.body.decode())
            db = SessionLocal()
            db_text = TextTable(datetime=datetime.now(), title=title, x_avg_count_in_line=x)
            db.add(db_text)
            db.commit()
            db.refresh(db_text)
            db.close()

    # Устанавливаем функцию обратного вызова для обработки сообщений из очереди
    await queue.consume(callback)
