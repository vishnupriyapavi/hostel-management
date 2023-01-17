from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import message
from django.shortcuts import render, redirect

from mainapp.forms import comp_form, review_form, room_form, student_form
from mainapp.models import hostel, food, fee, complaint, student, attendance, room, payment


@login_required(login_url='Login')
def student_view_hostel(request):
    data = hostel.objects.all()
    return render(request, 'student_view_hostel.html', {'data': data})

@login_required(login_url='Login')
def student_view_food(request):
    data = food.objects.all()
    return render(request, 'student_view_food.html', {'data': data})


@login_required(login_url='Login')
def student_view_fee(request):
    data = fee.objects.all()
    return render(request, 'student_view_fee.html', {'data': data})




@login_required(login_url='Login')
def student_add_complaint(request):
    form=comp_form()
    u=request.user
    if request.method=='POST':
        form=comp_form(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('student_view_reply')
    return render(request,'student_add_complaint.html',{'form':form})
@login_required(login_url='Login')
def student_view_reply(request):
    data = complaint.objects.filter(user=request.user)
    return render(request, 'student_view_reply.html', {'data': data})


@login_required(login_url='Login')
def student_add_review(request):
    form=review_form()
    if request.method=='POST':
        form=review_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')
    return render(request,'student_add_review.html',{'form':form})


@login_required(login_url='Login')
def student_view_attendance(request):
    u=student.objects.get(user=request.user)
    data = attendance.objects.filter(student_name=u)
    return render(request, 'student_view_attendance.html', {'data': data})


@login_required(login_url='Login')
def room_booking(request):
    form = room_form()
    if request.method == 'POST':
        form = room_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_room')
    return render(request, 'room_booking.html', {'form': form})
@login_required(login_url='Login')
def view_room(request):
    data = room.objects.all()
    return render(request, 'view_room.html', {'data': data})
# @login_required(login_url='Login')
# def student_approve_room(request):
#     booking1 = room.objects.get(id=id)
#     booking1.booking_status = 1
#     booking1.save()
#     messages.info(request, "approved student registration")
#     return redirect("view_room")
# @login_required(login_url='Login')
# def student_reject_room(request):
#     booking1 = room.objects.get(id=id)
#     booking1.booking_status = 2
#     booking1.save()
#     messages.info(request, "approved student registration")
#     return redirect("view_room")
@login_required(login_url='Login')
def student_update_room(request,id):
    room1 = room.objects.get(id=id)
    form = room_form(instance=room1)
    if request.method == "POST":
        form = room_form(request.POST, instance=room1)
    if form.is_valid():
        form.save()
        return redirect('view_room')
    return render(request, 'room_booking.html', {'form': form})
@login_required(login_url='Login')
def delete_room(request,id):
    room.objects.get(id=id).delete()
    return redirect('view_room')


@login_required(login_url='Login')
def student_view_profile(request):
    student1 = student.objects.get(user=request.user)
    return render(request,'student_view_profile.html',{'student1':student1})
@login_required(login_url='Login')
def student_update_profile(request):
    profile1 = student.objects.get(user=request.user)
    form = student_form(instance=profile1)
    if request.method == "POST":
        form = student_form(request.POST, instance=profile1)
    if form.is_valid():
        form.save()
        return redirect('student_view_profile')
    return render(request, 'student_update_profile.html', {'form': form})


@login_required(login_url='Login')
def delete_profile_student(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request,'Your Account Deleted Successfully')
        return redirect('index')
    return render(request,'delete_account.html')



@login_required(login_url='Login')
def view_studpay(request):
    data=payment.objects.all()
    return render(request,'view_studpay.html',{'data':data} )
@login_required(login_url='log')
def approve_payment(request,id):
    pay1=payment.objects.get(id=id)
    pay1.status = 1
    pay1.save()
    messages.info(request,"student paid succesfully")
    return redirect('view_studpay')


@login_required(login_url='log')
def reject_payment(request,id):
    pay1=payment.objects.get(id=id)
    pay1.status = 2
    pay1.save()
    messages.info(request,"not paid")
    return redirect('view_studpay')