from django.db import models


# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)


class Department(models.Model):
    departmentname = models.CharField(max_length=50)


class Course(models.Model):
    coursename = models.CharField(max_length=50)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)


class Subject(models.Model):
    subjectname = models.CharField(max_length=5000)
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)
    sem = models.CharField(max_length=50,default="")

class Staff(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100, default='')
    DEPRTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)
    place = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    district = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=300)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    yoj = models.DateField()
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Student(models.Model):
    admissionNo = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)
    place = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    pin = models.CharField(max_length=10)


class Allocate(models.Model):
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)
    SUBJECT = models.ForeignKey(Subject, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateField()


class Gallary(models.Model):
    image = models.CharField(max_length=300)
    date = models.DateField()
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Facility(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)


class Schedule(models.Model):
    programname = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.CharField(max_length=10)


class Support(models.Model):
    category = models.CharField(max_length=100)
    discription= models.CharField(max_length=100,default='')


class Complaints(models.Model):
    date = models.DateField()
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Feedback(models.Model):
    date = models.DateField()
    feedback = models.CharField(max_length=1000)
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Feedbackpublic(models.Model):
    date = models.DateField()
    feedback = models.CharField(max_length=1000)
    Email=models.CharField(max_length=100)


class Events(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=100)
    venue = models.CharField(max_length=50)
    time = models.CharField(max_length=10)
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Timetable(models.Model):
    day = models.CharField(max_length=10)
    hour = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

class Bus(models.Model):
    busno = models.CharField(max_length=10)
    place = models.CharField(max_length=50)

class Hostel(models.Model):
    facility = models.CharField(max_length=50)
    description=models.CharField(max_length=5000)

