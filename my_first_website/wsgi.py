import os
import sys
from django.core.wsgi import get_wsgi_application

# Vercel environment path adjustments
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_path not in sys.path:
    sys.path.append(base_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

application = get_wsgi_application()
app = application