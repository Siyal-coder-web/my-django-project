import os
import sys
from django.core.wsgi import get_wsgi_application

# Vercel runtime paths initialize karne ka sabse safe tareeqa
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

application = get_wsgi_application()
app = application