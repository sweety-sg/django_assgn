from django.contrib import admin
from .models import TodoList , TodoItem

admin.site.register(TodoItem)
admin.site.register(TodoList)

# Register your models here.
