from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


# Create your models here.

class TodoList(models.Model) :
    list_name = models.CharField(max_length=100 , validators=[MinLengthValidator(1)])

    def __str__(self) :
        return f"{self.list_name}"

class TodoItem(models.Model) :
    title = models.CharField(max_length=100, blank=False)
    checked = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    todo_list = models.ForeignKey(to = TodoList, on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.todo_list.list_name} : {self.title}"
