from rest_framework import serializers
from .models import Student,EmployeeModel,Course,CourseDetails



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = "__all__"

class CourseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetails
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    display_course_details = CourseDetailsSerializer(read_only=True,many=True)
    class Meta:
        model = Course
        fields = "__all__"




'''
class StudentSerializer(serializers.Serializer):
    #id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

def create(self,validate_data):
    return Student.objects.create(**validate_data)

'''