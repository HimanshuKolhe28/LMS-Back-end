from django.db import models

from django.contrib.auth.models import User


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    branch = models.CharField(max_length=100)
    year = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'