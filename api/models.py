from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)


class EmployeeModel(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salary = models.IntegerField()

    class Meta:
        db_table = 'employee'

class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'courses'

class CourseDetails(models.Model):
    cname = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    fees = models.IntegerField()
    courses = models.ForeignKey(Course,related_name="display_course_details",on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'course_details'