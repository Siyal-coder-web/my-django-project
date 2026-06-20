import os
import sys
from django.core.wsgi import get_wsgi_application

# Root directory ko path mein shamil kar rahe hain
sys.path.append(os.path.dirname(__file__))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

application = get_wsgi_application()
app = application