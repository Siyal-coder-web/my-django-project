import os
import sys
from django.core.wsgi import get_wsgi_application

# Vercel ko inner modules locate karwane ke liye system path definition
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

application = get_wsgi_application()
app = application