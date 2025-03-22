# Base image
FROM python:3.11-slim

# Upgrade pip (Recommended)
RUN pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start Django server using Gunicorn
CMD ["gunicorn", "dreamers_blog_project.wsgi:application", "--bind", "0.0.0.0:8000"]
