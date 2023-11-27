# AsyncMessagesQueue
Тестовое задание для компании "BAUM STORAGE"

Это асинхронное FastAPI-приложение, взаимодействующее с RabbitMQ для обмена сообщениями, и использующее PostgreSQL в качестве базы данных, и SQLAlchemy в качесте ORM системы.
Так же использует Pydantic для обработки входящих данных.

Принимает в себя параметры: datetime(str), title(str), text(str). Отправляет весь запрос в RabbitMQ, далее когда мы получаем эти данные из RabbitMQ ,они отправляются в БД, считается среднее колличество "X" в тексте за каждую строчку и сохраняет его как "x_avg_count_in_line". Далее при запросе "/get-x", возвращает все данные из БД по ID(ID скрыт и не показывается).   

Приложение упаковано в контейнеры с использованием Docker и управляется с помощью Docker Compose.

## Использование
- Используйте `/count-x-from-text`, чтобы загружать сообщения в RabbitMQ в JSON формате.

Принимает в себя JSON:

```json
[
  {
    "datetime": "15.11.2023 15:00:25.001",
    "title": "Very fun book",
    "text": "...Rofl...lol../n..ololo..."
  },
  {
    "datetime": "18.01.2023 12:00:25.001",
    "title": "Other very fun book",
    "text": "...nice...lol../n..XxxloXX..."
  }
]
```

- Используйте `/get-x`, чтобы получать результаты из базы данных PostgreSQL.
  
Возвращает:

```json
[
  {
    "datetime": "15.11.2023 15:00:25.001",
     "title": "Very fun book",
     "x_avg_count_in_line": 0.012
  },
  {
    "datetime": "18.01.2023 12:00:25.001",
    "title": "Other very fun book",
    "x_avg_count_in_line": 0.032
  }
]
```

## Запуск

Перед запуском не забудьте создать и активировать виртуальное окружение

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
   
6. Ваше FastAPI-приложение будет доступно по адресу http://localhost:8888.



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

