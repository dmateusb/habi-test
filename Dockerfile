FROM python:3.8.10

RUN mkdir app
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1
COPY . .
EXPOSE 8000
EXPOSE 8001