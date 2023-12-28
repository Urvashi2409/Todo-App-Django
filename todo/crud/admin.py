from django.contrib import admin
from .models import TodoItem

# Register your models here.
admin.site.register(TodoItem)

# whenever you do some changes to the models.py then always run two commands: 
# python manage.py makemigrations 
# python manage.py migrate 
