from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_parent=models.BooleanField(default=False)

class student(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,primary_key=True,related_name='student')
    name=models.CharField(max_length=30)
    registration_id=models.CharField(max_length=10)
    contact_no=models.CharField(max_length=10)
    Email_address=models.EmailField()
    Address=models.CharField(max_length=100)
    approval_status=models.IntegerField(default=0)
    profile_image=models.ImageField(upload_to='profile')


    def __str__(self):
        return self.name

class parent(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,primary_key=True,related_name='parent')
    name=models.CharField(max_length=30)
    student_name=models.ForeignKey(student,on_delete=models.CASCADE)
    registration_id=models.CharField(max_length=10)
    contact_no=models.CharField(max_length=10)
    Email=models.EmailField()
    Address=models.CharField(max_length=100)
    approval_status=models.IntegerField(default=0)


    def __str__(self):
        return self.name

class hostel(models.Model):
    hostel_name=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    fee_details=models.CharField(max_length=100)
    room_details=models.CharField(max_length=100)
    contact_no=models.IntegerField()
    hostel_image=models.ImageField(upload_to='hostel')

    def __str__(self):
        return self.hostel_name



class food(models.Model):
    breakfast=models.CharField(max_length=20)
    lunch=models.CharField(max_length=20)
    snacks=models.CharField(max_length=20)
    dinner=models.CharField(max_length=20)

class staff(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    contact_no=models.IntegerField()

    def __str__(self):
        return self.name


class notification(models.Model):
    date=models.DateField()
    massege=models.CharField(max_length=100)

class fee(models.Model):
    hostel_name=models.ForeignKey(hostel,on_delete=models.CASCADE)
    mess_bill=models.FloatField(default=0)
    room_rent=models.FloatField(default=0)
    amount=models.FloatField(default=0)

    def __str__(self):
         return self.amount



class complaint(models.Model):
    user=models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date=models.DateField(auto_now=True)
    complaint=models.CharField(max_length=30)
    reply=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user


class review(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateField()
    review=models.CharField(max_length=100)
    # replay=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class attendance(models.Model):
    student_name = models.ForeignKey(student,on_delete=models.DO_NOTHING)
    date = models.DateField()
    attendance = models.CharField(max_length=10)

    def __str__(self):
        return self.student_name

class room(models.Model):
    name=models.CharField(max_length=100)
    joining_date=models.DateField()
    booking_date=models.DateField()
    booking_status=models.IntegerField(default=0)
    room_type=models.CharField(max_length=100)

class payment(models.Model):
    student_name = models.ForeignKey(student,on_delete=models.CASCADE)
    room_rent = models.IntegerField(default=0)
    mess_bill = models.IntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    amount = models.IntegerField(default=0)
    status =  models.IntegerField(default=0)

    def __str__(self):
        return self.student_name