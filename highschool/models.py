from django.db import models

# Create your models here.


class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    firstName = models.CharField(max_length=100)

    lastName = models.CharField(max_length=100)

    age = models.IntegerField()

    gender = models.CharField(max_length=10, choices= GENDER_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"