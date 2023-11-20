import pika
from config import RABBITMQ_URL, EXCHANGE_NAME

# Переменне из окружения для rabbitmq
RABBITMQ_URL = RABBITMQ_URL
EXCHANGE_NAME = EXCHANGE_NAME


def sent_to_rabbit(message: str):
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


def count_x(message: str):
    # Ваш исходный текст

    # Разделение текста по переходам на новую строку
    lines = message.split('\n')

    # Подсчет количества вхождений буквы "X"
    count_of_X = sum(line.count('X') + line.count('x') for line in lines)
    average_of_X_per_line = count_of_X / len(lines) if len(lines) > 0 else 0

    # Вывод результатов
    return average_of_X_per_line


# def count_x2(mess: str):
#     texts = mess
#     results = []
#
#     for text in texts:
#         x_count = text.count("X")
#         x_avg_count_in_line = x_count / len(text) if len(text) > 0 else 0.0
#         # results.append(Result(datetime=str(text.datetime), title=text.title, x_avg_count_in_line=x_avg_count_in_line))
#         results.append(x_avg_count_in_line)
#
#     print(results)
