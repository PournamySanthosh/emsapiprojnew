from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your super models here with some change
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#Creating a dept model class by inheriting the model class
class Department(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=200)
#instead of the memory address of the object,
#we need to return the name of the dept
    def __str__(self):
        return self.DepartmentName
    
class Employee(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=200)
    Designation=models.CharField(max_length=150)
    Dateofjoining=models.DateField()
    #depid is a foreign key from dept table
    DepartmentId=models.ForeignKey(Department,on_delete=models.CASCADE)
    Contact=models.CharField(max_length=150)
    IsActive=models.BooleanField(default=True)

    def __str__(self):
        return self.EmployeeName

