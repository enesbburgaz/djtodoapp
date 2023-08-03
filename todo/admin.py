from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    model= Todo
    list_display = ['title','created','updated','status']

admin.site.register(Todo, TodoAdmin)
