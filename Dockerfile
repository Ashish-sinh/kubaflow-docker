FROM python:3.11-slim

COPY requirements.txt .

RUN pip install -r requirements.txt 

RUN mkdir -p /app

COPY ./app app 

EXPOSE 80 

CMD [ "uvicorn","app.main:main", "--host", "0.0.0.0", "--port", "80"]
