import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

# Root directory ko path mein shamil kar rahe hain
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_website.settings')

try:
    # Yeh command cloud par aate hi saare missing tables (auth_user wagera) khud bana degi
    call_command('migrate', interactive=False)
except Exception as e:
    print("Migration Error:", e)

application = get_wsgi_application()
app = application