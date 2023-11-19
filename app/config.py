import os
from dotenv import load_dotenv

# Импорт переменных окружения
load_dotenv()

POSTGRESQL_URL = os.environ.get('POSTGRESQL_URL')
RABBITMQ_URL = os.environ.get('RABBITMQ_URL')
EXCHANGE_NAME = os.environ.get('EXCHANGE_NAME')
