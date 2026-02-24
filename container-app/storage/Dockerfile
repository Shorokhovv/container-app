FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/storage

ENV APP_PORT=8000


VOLUME ["/app/storage"]

EXPOSE $APP_PORT
 
CMD python app.py