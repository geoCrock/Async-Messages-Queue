#AsyncMessagesQueue

It is an asynchronous FastAPI application that interacts with RabbitMQ for messaging, and uses PostgreSQL as a database and SQLAlchemy as an ORM system.
It also uses Pydantic to process incoming data.

Accepts parameters: datetime(str), title(str), text(str). Sends the entire request to RabbitMQ, then when we receive this data from RabbitMQ, it is sent to the database, the average number of “X” in the text for each line is calculated and saved as “x_avg_count_in_line”. Next, when requesting “/get-x”, it returns all data from the database by ID (ID is hidden and not shown).

The application is containerized using Docker and managed using Docker Compose.

## Usage
- Use `/count-x-from-text` to load messages into RabbitMQ in JSON format.

Accepts JSON:

```json
[
   {
     "datetime": "11/15/2023 15:00:25.001",
     "title": "Very fun book",
     "text": "...Rofl...lol../n..ololo..."
   },
   {
     "datetime": "01/18/2023 12:00:25.001",
     "title": "Other very fun book",
     "text": "...nice...lol../n..XxxloXX..."
   }
]
```

- Use `/get-x` to get results from a PostgreSQL database.
  
Returns:

```json
[
   {
     "datetime": "11/15/2023 15:00:25.001",
      "title": "Very fun book",
      "x_avg_count_in_line": 0.012
   },
   {
     "datetime": "01/18/2023 12:00:25.001",
     "title": "Other very fun book",
     "x_avg_count_in_line": 0.032
   }
]
```

## Launch

Before starting, do not forget to create and activate a virtual environment

1. Clone the repository:

     ```bash
     git clone https://github.com/geoCrock/AsyncMessagesQueue.git
     ```

2. Go to the project directory:

     ```bash
     cd AsyncMessagesQueue
     ```

3. Create a `.env` file in the project root and specify the necessary environment variables:

    Example:
     ```env
     POSTGRES_URL = "postgresql://postgresql:postgresql@localhost/countx"
    
     RABBITMQ_URL = "amqp://guest:guest@localhost/"
     ```

    Specify your parameters
   
5. Run main.py in the app folder:
    ```bash
     cd app
     ```

    ```bash
     main.py
     ```
   
6. Your FastAPI application will be available at http://localhost:8888.



## Running via Docker

Make sure the following components are installed on your system:

-Docker
- Docker Compose

1. Clone the repository:

     ```bash
     git clone https://github.com/geoCrock/AsyncMessagesQueue.git
     ```

2. Go to the project directory:

     ```bash
     cd AsyncMessagesQueue
     ```

3. Create a `.env` file in the project root and specify the necessary environment variables:


    Example:
     ```env
     POSTGRES_URL = "postgresql://postgresql:postgresql@localhost/countx"
    
     RABBITMQ_URL = "amqp://guest:guest@localhost/"
     ```

    Specify your parameters

5. Build and run Docker containers:

     ```bash
     docker-compose up --build
     ```

6. Your FastAPI application will be available at [http://localhost:8888](http://localhost:8888).
