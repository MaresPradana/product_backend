FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    pkg-config \
    libffi-dev \
    libssl-dev \
    build-essential \
    libmariadb-dev \
    mariadb-client

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "product_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
