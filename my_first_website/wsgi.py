import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

# Path issues fix karne ke liye
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

# Server start hote hi database tables deploy/create karega
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print("Auto Migration Error:", e)

application = get_wsgi_application()
app = application