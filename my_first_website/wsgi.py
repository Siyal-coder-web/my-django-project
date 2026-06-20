import os
import sys
from django.core.wsgi import get_wsgi_application

# Vercel ko root directory samjhane ke liye path set kar rahe hain
path = os.path.dirname(os.path.dirname(__file__))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

try:
    application = get_wsgi_application()
    app = application
except Exception as e:
    print(f"WSGI Loading Error: {e}")
    raise e