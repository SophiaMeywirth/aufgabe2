from django.db import models

class Todo(models.Model):
    todo_text = models.CharField(max_length=160)
    due_date = models.DateTimeField('date due')
    percent_finished = models.CharField(max_length=5)
    def __str__(self):
    	return self.todo_text
