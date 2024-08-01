from django.db import models
from django.contrib.auth.models import User

class todo(models.Model):
    todo_name = models.CharField(max_length=250)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.todo_name