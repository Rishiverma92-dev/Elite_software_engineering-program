from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=1000)
    stu_class = models.CharField(max_length=500)
    roll_no = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.name , self.roll_no
    