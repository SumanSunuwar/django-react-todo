from django.contrib import admin
from .models import Todo,Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title',)

class TodoAdmin(admin.ModelAdmin):  
    list_display = ('category','title', 'description', 'date')  




# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Todo, TodoAdmin)  