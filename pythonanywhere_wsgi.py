#!/usr/bin/python3.10

import os
import sys

# Add your project directory to the sys.path
# Replace 'yourusername' with your actual PythonAnywhere username
path = '/home/padimi/String-Analyzer-Service/String_Analyzer_Service_BE'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'stringanalyzerservice.settings'

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv('/home/padimi/String-Analyzer-Service/String_Analyzer_Service_BE/.env')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()