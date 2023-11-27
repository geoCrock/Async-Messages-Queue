FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888"]
