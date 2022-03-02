from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Parent category for todos (fields : title)
class Task(models.Model):
	task_title = models.CharField(max_length=225)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.task_title


# fields : title , description, date
class Todo(models.Model):
	category = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	date = models.DateField(null=True,blank=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self) -> str:
		return self.title