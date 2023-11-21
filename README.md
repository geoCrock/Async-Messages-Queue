# AsyncMessagesQueue
Тестовое задание для компании "BAUM STORAGE"

Это асинхронное FastAPI-приложение, взаимодействующее с RabbitMQ для обмена сообщениями и использующее PostgreSQL в качестве базы данных. Приложение упаковано в контейнеры с использованием Docker и управляется с помощью Docker Compose.

## Запуск

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/geoCrock/AsyncMessagesQueue.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd AsyncMessagesQueue
    ```

3. Создайте файл `.env` в корне проекта и укажите необходимые переменные окружения:

   Пример:
    ```env
    POSTGRES_URL = "postgresql://postgresql:postgresql@localhost/countx"
    
    RABBITMQ_URL = "amqp://guest:guest@localhost/"
    ```

   Указывайте ваши параметры
   
5. Запустите main.py в папке app:
   ```bash
    cd app
    ```

   ```bash
    main.py
    ```

   
## Использование

- Используйте `/count-x-from-text`, чтобы загружать сообщения в RabbitMQ в JSON формате.
- Используйте `/get-x`, чтобы получать результаты из базы данных PostgreSQL.


## Запуск через Docker 

Убедитесь, что на вашей системе установлены следующие компоненты:

- Docker
- Docker Compose

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/geoCrock/AsyncMessagesQueue.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd AsyncMessagesQueue
    ```

3. Создайте файл `.env` в корне проекта и укажите необходимые переменные окружения:


   Пример:
    ```env
    POSTGRES_URL = "postgresql://postgresql:postgresql@localhost/countx"
    
    RABBITMQ_URL = "amqp://guest:guest@localhost/"
    ```

   Указывайте ваши параметры

5. Соберите и запустите Docker-контейнеры:

    ```bash
    docker-compose up --build
    ```

6. Ваше FastAPI-приложение будет доступно по адресу [http://localhost:8888](http://localhost:8888).

## Использование

- Используйте `/count-x-from-text`, чтобы загружать сообщения в RabbitMQ в JSON формате.
- Используйте `/get-x`, чтобы получать результаты из базы данных PostgreSQL.
