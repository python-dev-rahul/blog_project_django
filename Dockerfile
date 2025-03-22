# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start Django server
CMD ["gunicorn", "dreamers_blog_project.wsgi:application", "--bind", "0.0.0.0:8000"]
