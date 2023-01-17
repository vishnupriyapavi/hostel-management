import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from mainapp.models import student, parent, Login, hostel, food, staff, notification, fee, complaint, review, \
    attendance, room, payment


class DateInput(forms.DateInput):
    input_type = 'date'

def phone_number_validator(value):
    if not re.compile(r'^[6-9]\d{9}$').match(value):
        raise ValidationError('This is not a valid number')

class loginregister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2')


class student_form(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    Email_address=forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$',message='Please enter a valid email')])

    class Meta:
            model = student
            exclude=('user','approval_status',)
    def clean_email(self):
        mail=self.cleaned_data["Email_address"]
        parent_mail=parent.objects.filter(Email_address=mail)
        student_mail=student.objects.filter(Email_address=mail)

        if parent_mail.exists():
            raise forms.ValidationError("This email already registerd")
        if student_mail.exists():
            raise forms.ValidationError("This email already registerd")
        return mail

    def clean_phone(self):
        phone=self.cleaned_data["contact_no"]
        parent_phone=parent.objects.filter(contact_no=phone)
        student_phone=student.objects.filter(contact_no=phone)

        if parent_phone.exists():
            raise forms.ValidationError("This phone already registerd")
        if student_phone.exists():
            raise forms.ValidationError("This phone already registerd")
        return phone


class parent_form(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    Email=forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$',message='Please enter a valid email')])
    class Meta:
        model = parent
        exclude = ('user','approval_status',)
    def clean_email(self):
        mail = self.cleaned_data["Email"]
        parent_mail = parent.objects.filter(Email=mail)
        student_mail = student.objects.filter(Email=mail)
        if parent_mail.exists():
            raise forms.ValidationError("This email already registerd")
        if student_mail.exists():
            raise forms.ValidationError("This email already registerd")
        return mail
    def clean_phone(self):
        phone = self.cleaned_data["contact_no"]
        parent_phone = parent.objects.filter(contact_no=phone)
        student_phone = student.objects.filter(contact_no=phone)
        if parent_phone.exists():
            raise forms.ValidationError("This phone already registerd")
        if student_phone.exists():
            raise forms.ValidationError("This phone already registerd")
        return phone

class hostel_form(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = hostel
        fields = '__all__'

class food_form(forms.ModelForm):
    class Meta:
        model = food
        fields = '__all__'

class staff_form(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = staff
        fields = '__all__'

class notification_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = notification
        fields = '__all__'



class fee_form(forms.ModelForm):
        date=forms.DateField(widget=DateInput)
        class Meta:
            model=fee
            fields='__all__'

class comp_form(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model = complaint
        exclude = ('reply','user',)

class reply(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model = complaint
        exclude =('user','date','complaint',)

class review_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = review
        fields = '__all__'


attendance_choice = (
    ('present','present'),
    ('absent','absent')
)

class attendance_form(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    attendance=forms.ChoiceField(choices=attendance_choice,widget=forms.RadioSelect)

    class Meta:
        model = attendance
        fields = '__all__'

room_type_choice = (
    ('single','single'),
    ('double','double')
)

class room_form(forms.ModelForm):
    joining_date=forms.DateField(widget=DateInput)
    booking_date=forms.DateField(widget=DateInput)
    room_type=forms.ChoiceField(choices=room_type_choice,widget=forms.RadioSelect)
    class Meta:
        model = room
        fields = '__all__'
        exclude = ('booking_status',)

class paymentform(forms.ModelForm):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    class Meta:
        model = payment
        fields ="__all__"
        exclude = ('status',)