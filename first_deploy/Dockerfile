# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the container
COPY . /app/

# Collect static files (optional)
RUN python manage.py collectstatic --noinput

# Open port 8000 for the app
EXPOSE 8000

# Run Gunicorn (make sure it's installed)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]
