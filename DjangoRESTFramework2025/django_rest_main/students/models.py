from django.db import models

# Create your models here.

class Student(models.Model):

    student_id = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=200)


    def __str__(self):
        return self.name