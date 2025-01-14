from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    table = models.CharField(max_length=20)
    status = models.BooleanField(default=False)

class Booking_drink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)

