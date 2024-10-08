# Use the official Python image from the Docker Hub
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Run Django migrations and collect static files
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn project.wsgi:application --bind 0.0.0.0:8000"]
