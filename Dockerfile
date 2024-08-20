# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Make wait-for-it.sh executable
RUN chmod +x wait-for-it.sh

# Start the server after waiting for MySQL and running migrations
CMD ["sh", "-c", "./wait-for-it.sh db:3306 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
