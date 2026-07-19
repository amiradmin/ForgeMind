FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements/ ./requirements/


RUN pip install --upgrade pip && \
    pip install -r requirements/development.txt


COPY . .


RUN mkdir -p /app/logs \
    && mkdir -p /app/celery


EXPOSE 8000

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]