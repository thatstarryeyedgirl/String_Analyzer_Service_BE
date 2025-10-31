#!/usr/bin/python3.10

import os
import sys

from dotenv import load_dotenv

# Add your project directory to the sys.path
path = '/home/padimi/String-Analyzer-Service'
if path not in sys.path:
    sys.path.insert(0, path)

# Load environment variables from .env file
load_dotenv('/home/padimi/String-Analyzer-Service/.env')

from django.core.wsgi import get_wsgi_application
# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'stringanalyzerservice.settings'

application = get_wsgi_application()

