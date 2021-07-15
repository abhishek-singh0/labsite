from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django_extensions.db.models import TimeStampedModel

class Projects(TimeStampedModel):
    title=models.CharField(max_length=100)
    desription=models.CharField(max_length=1000,blank=True)
    pass

class Assignments(TimeStampedModel):
    class Status(models.TextChoices):
        COMPLETED="Completed"
        PENDING="Pending"   
        BACKLOG="Backlog"

    user=models.ForeignKey(User,on_delete=models.PROTECT)
    project=models.ForeignKey(Projects,on_delete=models.PROTECT) #need to verify this
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=1000,blank=True)
    status=models.CharField(max_length=20,default=Status.PENDING,choices=Status.choices)
    due_date=models.DateField()
    pass

class comments(TimeStampedModel):
    assignment=models.ForeignKey(Assignments,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    body=models.CharField(max_length=150,blank=True)
    pass

