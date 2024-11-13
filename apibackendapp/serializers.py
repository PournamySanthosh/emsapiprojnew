from rest_framework import serializers #import module
from .models import Employee, Department
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password
class SignupSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(write_only=True, required=False)
    def create(self, validated_data):
        group_name = validated_data.pop("group_name",None)
        validated_data['password'] = make_password(validated_data.get("password"))
        user = super(SignupSerializer,self).create(validated_data)
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
        return user

    class Meta:
         model = User
         fields = ['username', 'password', 'group_name']


#create serializer by inheriting modelserializer class
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields=['username','password']
        

            




#create serializer by inherting ModelSerializer class
class DepartmentSerializer(serializers.ModelSerializer) :
    class Meta: 
        model = Department
        fields=('DepartmentId','DepartmentName')
#validation for employeename
def name_validation(employee_name):
    if len(employee_name)<3:
        raise serializers.ValidationError("Name must be atleast 3 characters ")
    return employee_name
        

class EmployeeSerializer(serializers.ModelSerializer) :
#dpt is a custom field in the serializer
    Department = DepartmentSerializer(source='DepartmentId',read_only=True)
    #adding validation to the field employeename
    EmployeeName = serializers.CharField(max_length=200, validators =[name_validation])
    class Meta: 
        model = Employee
        fields= ('EmployeeId','EmployeeName','Designation','Dateofjoining','IsActive','DepartmentId','Department')


class UserSerializer(serializers.ModelSerializer) :
    class Meta: 
        model = User
        fields= ('id','username') #get only these two fields
        