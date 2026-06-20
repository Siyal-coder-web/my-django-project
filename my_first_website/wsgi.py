import os
import sys
from django.core.wsgi import get_wsgi_application

# Global environment injection ko handle karne ke liye
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

try:
    application = get_wsgi_application()
    app = application
except Exception as e:
    print(f"Critical WSGI Failure: {e}")
    raise e