#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create superuser with hardcoded credentials
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "admin"
email = "admin@example.com"
password = "admin12345"  # Cambia esto por una contraseña segura
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superusuario creado exitosamente")
else:
    print("Superusuario ya existe, se omite la creación")
EOF
