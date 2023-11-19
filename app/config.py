import os
from dotenv import load_dotenv

# Импорт переменных окружения
load_dotenv()

POSTGRESQL_URL = os.environ.get('POSTGRESQL_URL')
