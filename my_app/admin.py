from django.contrib import admin
from .models import Project

# Hum Django ko bata rahe hain ke humein admin panel mein yeh table dikhao
admin.site.register(Project)