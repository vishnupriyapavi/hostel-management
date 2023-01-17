from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from mainapp.forms import hostel_form, food_form, staff_form, notification_form, fee_form, comp_form, review_form, \
    attendance_form, room_form, reply, paymentform
from mainapp.models import student, parent, hostel, food, staff, notification, fee, complaint, review, attendance, room, \
    payment


def student_view(request):
    data = student.objects.all()
    return render(request,'view.html',{'data':data})

def approve_student(request,id):
    student1 = student.objects.get(user_id=id)
    student1.approval_status=1
    student1.save()
    messages.info(request,' Student Approved')
    return redirect('admin1')

def reject_student(request, id):
    Student=student.objects.get(user_id=id)
    Student.approval_status=2
    Student.save()
    messages.info(request,'Rejected')
    return redirect('admin1')

def parent_view(request):
    data=parent.objects.all()
    return render(request,'parent_view.html',{'data':data})

def approve_parent(request,id):
    parent1=parent.objects.get(user_id=id)
    parent1.approval_status = 1
    parent1.save()
    messages.info(request,'Approved')
    return redirect('parent_view')

def reject_parent(request, id):
    parent1=parent.objects.get(user_id=id)
    parent1.approval_status = 2
    parent1.save()
    messages.info(request,'Rejected')
    return redirect('parent_view')

# hostel
@login_required(login_url='Login')
def add_hostel(request):
    form=hostel_form()
    if request.method=='POST':
        form=hostel_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin1')
    return render(request,'add_hostel.html',{'form':form})
@login_required(login_url='Login')
def view_hostel(request):
    data = hostel.objects.all()
    return render(request, 'view_hostel.html', {'data': data})
@login_required(login_url='Login')
def hostel_update(request,id):
    hostel1=hostel.objects.get(id=id)
    form=hostel_form(instance=hostel1)
    if request.method=="POST":
        form=hostel_form(request.POST,instance=hostel1)
    if form.is_valid():
        form.save()
        return redirect('view_hostel')
    return render(request,'add_hostel.html',{'form':form})
@login_required(login_url='Login')
def hostel_delete(request,id):
    hostel.objects.get(id=id).delete()
    return redirect('view_hostel')

# food
@login_required(login_url='Login')
def add_food(request):
    form=food_form()
    if request.method=='POST':
        form=food_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin1')
    return render(request,'add_food.html',{'form':form})
@login_required(login_url='Login')
def view_food(request):
    data = food.objects.all()
    return render(request, 'view_food.html', {'data': data})
@login_required(login_url='Login')
def food_update(request,id):
    food1=food.objects.get(id=id)
    form=food_form(instance=food1)
    if request.method=="POST":
        form=food_form(request.POST,instance=food1)
    if form.is_valid():
        form.save()
        return redirect('view_food')
    return render(request,'add_food.html',{'form':form})
@login_required(login_url='Login')
def food_delete(request,id):
    food.objects.get(id=id).delete()
    return redirect('view_food')


# staff
@login_required(login_url='Login')
def add_staff(request):
    form=staff_form()
    if request.method=='POST':
        form=staff_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    return render(request,'add_staff.html',{'form':form})
@login_required(login_url='Login')
def view_staff(request):
    data = staff.objects.all()
    return render(request, 'view_staff.html', {'data': data})
@login_required(login_url='Login')
def staff_update(request,id):
    staff1=staff.objects.get(id=id)
    form=staff_form(instance=staff1)
    if request.method=="POST":
        form=staff_form(request.POST,instance=staff1)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request,'add_staff.html',{'form':form})
@login_required(login_url='Login')
def staff_delete(request,id):
    staff.objects.get(id=id).delete()
    return redirect('view_staff')


# notification
@login_required(login_url='Login')
def add_notification(request):
    form=notification_form()
    if request.method=='POST':
        form=notification_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin1')
    return render(request,'add_notification.html',{'form':form})
@login_required(login_url='Login')
def view_notification(request):
    data = notification.objects.all()
    return render(request, 'view_notification.html', {'data': data})
@login_required(login_url='Login')
def notification_update(request,id):
    noti1=notification.objects.get(id=id)
    form=notification_form(instance=noti1)
    if request.method=="POST":
        form=notification_form(request.POST,instance=noti1)
    if form.is_valid():
        form.save()
        return redirect('view_notification')
    return render(request,'add_notification.html',{'form':form})
@login_required(login_url='Login')
def notification_delete(request,id):
    notification.objects.get(id=id).delete()
    return redirect('view_notification')



# fee
@login_required(login_url='Login')
def add_fee(request):
    form = fee_form()
    if request.method == 'POST':
        form = fee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_fee')
    return render(request,'add_fee.html',{'form':form})

# @login_required(login_url='Login')
# def view_payment(request):
#     payment = fee.objects.filter(status=1)
#     return render(request, 'view_payment.html', {'payments': payment})


# def add_fee(request):
    # form=fee_form()
    # if request.method=='POST':
    #     form=fee_form(request.POST,request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('admin1')
    # return render(request,'add_fee.html',{'form':form})
@login_required(login_url='Login')
def view_fee(request):
    data = fee.objects.all()
    return render(request, 'view_fee.html', {'data': data})
@login_required(login_url='Login')
def fee_update(request,id):
    fee1=fee.objects.get(id=id)
    form=fee_form(instance=fee1)
    if request.method=="POST":
        form=fee_form(request.POST,instance=fee1)
    if form.is_valid():
        form.save()
        return redirect('view_fee')
    return render(request,'add_fee.html',{'form':form})
@login_required(login_url='Login')
def fee_delete(request,id):
    fee.objects.get(id=id).delete()
    return redirect('view_fee')




# complaint
@login_required(login_url='Login')
def view_complaint(request):
    data = complaint.objects.all()
    return render(request, 'view_complaint.html', {'data': data})
@login_required(login_url='Login')
def reply_com(request,id):
    f=complaint.objects.get(id=id)
    if request.method == 'POST':
        r=request.POST.get('reply')
        f.reply=r
        f.save()
        return redirect('view_complaint')
    return render(request, 'reply_com.html', {'f': f})


# @login_required(login_url='Login')
# def comp_update(request,id):
#     com1=complaint.objects.get(id=id)
#     form=comp_form(instance=com1)
#     if request.method=="POST":
#         form=comp_form(request.POST,instance=com1)
#     if form.is_valid():
#         form.save()
#         return redirect('admin1')
#     return render(request,'view_complaint.html',{'form':form})
# @login_required(login_url='Login')
# def comp_delete(request,id):
#     complaint.objects.get(id=id).delete()
#     return redirect('view_complaint')


# review
@login_required(login_url='Login')
def view_review(request):
    data = review.objects.all()
    return render(request,'view_review.html',{'data': data})
@login_required(login_url='Login')
def review_update(request,id):
    re1=review.objects.get(id=id)
    form=review_form(instance=re1)
    if request.method=="POST":
        form=review_form(request.POST,instance=re1)
    if form.is_valid():
        form.save()
        return redirect('admin1')
    return render(request,'view_review.html',{'form':form})
@login_required(login_url='Login')
def review_delete(request,id):
    review.objects.get(id=id).delete()
    return redirect('view_review')


#!!!!!!!!!!!_____________attendance_______________!!!!!!!
@login_required(login_url='Login')
def add_attendance(request):
    form=attendance_form()
    if request.method=='POST':
        form=attendance_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    return render(request,'add_attendance.html',{'form':form})
@login_required(login_url='Login')
def view_attendance(request):
    data = attendance.objects.all()
    return render(request, 'view_attendance.html', {'data': data})
@login_required(login_url='Login')
def attendance_update(request,id):
    attendance1=attendance.objects.get(id=id)
    form=attendance_form(instance=attendance1)
    if request.method=="POST":
        form=attendance_form(request.POST,instance=attendance1)
    if form.is_valid():
        form.save()
        return redirect('view_attendance')
    return render(request,'add_attendance.html',{'form':form})
@login_required(login_url='Login')
def attendance_delete(request,id):
    attendance.objects.get(id=id).delete()
    return redirect('view_attendance')

# room
@login_required(login_url='Login')
def admin_view_room(request):
    data = room.objects.all()
    return render(request, 'admin_view_room.html', {'data': data})
@login_required(login_url='Login')
def admin_add_room(request):
    form=room_form()
    if request.method=='POST':
        form=room_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_view_room')
    return render(request,'admin_add_room.html',{'form':form})
@login_required(login_url='Login')
def approve_booking(request,id):
    booking1=room.objects.get(id=id)
    booking1.booking_status=1
    booking1.save()
    messages.info(request,"approved student registration")
    return redirect("admin_view_room")

@login_required(login_url='Login')
def reject_booking(request,id):
    booking1=room.objects.get(id=id)
    booking1.booking_status=2
    booking1.save()
    messages.info(request,"Rejectd student registration")
    return redirect("admin_view_room")

# !!!!___________payment___________!!!
@login_required(login_url='Login')
def add_admin_pay(request):
    form = paymentform()
    if request.method == "POST":
        form = paymentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_pay')
    return render(request,'add_adminpay.html',{'form':form})


@login_required(login_url='Login')
def view_pay(request):
    data = payment.objects.all()
    return render(request,'admin_viewpay.html',{'data':data})


@login_required(login_url='Login')
def pay_update(request,id):
    payment1=payment.objects.get(id=id)
    form=paymentform(instance=payment1)
    if request.method=="POST":
        form=paymentform(request.POST,instance=payment1)
    if form.is_valid():
        form.save()
        return redirect('view_pay')
    return render(request,'add_adminpay.html',{'form':form})


@login_required(login_url='Login')
def pay_delete(request,id):
    payment.objects.get(id=id).delete()
    return redirect('view_pay')
