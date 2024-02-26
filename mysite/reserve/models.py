from django.db import models
from datetime import time

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'Table {self.table_number}'

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('รอดำเนินการ', 'Pending'),
        ('ยอนรับ', 'Approved'),
        ('ปฏิเสธ', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    num_people = models.IntegerField()
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f'Reservation for {self.name} at Table {self.table.table_number}'