import os
import sys
from django.core.wsgi import get_wsgi_application

# Vercel runtime path insertion handle karne ke liye
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

application = get_wsgi_application()
app = application