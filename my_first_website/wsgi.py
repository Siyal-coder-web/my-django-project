import os
import sys
from django.core.wsgi import get_wsgi_application

# Project ke root folder ka absolute path nikal kar system path mein add karna
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Settings module ko environment mein set karna
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

application = get_wsgi_application()
app = application