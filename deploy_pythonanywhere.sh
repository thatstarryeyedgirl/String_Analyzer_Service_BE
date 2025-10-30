#!/bin/bash

# PythonAnywhere Deployment Script
# Run this in your PythonAnywhere bash console

echo "Installing dependencies..."
pip3.10 install --user -r requirements_pythonanywhere.txt

echo "Collecting static files..."
python3.10 manage.py collectstatic --noinput

echo "Running migrations..."
python3.10 manage.py migrate

echo "Deployment complete!"
echo "Don't forget to:"
echo "1. Update ALLOWED_HOSTS in settings.py with your domain"
echo "2. Configure the WSGI file in the Web tab"
echo "3. Set up static files mapping: /static/ -> /home/yourusername/String-Analyzer-Service/static/"