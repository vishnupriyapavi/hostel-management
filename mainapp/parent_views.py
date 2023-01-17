from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mainapp.models import hostel, attendance, staff, fee, room, payment


@login_required(login_url='Login')
def parent_view_hostel(request):
    data = hostel.objects.all()
    return render(request, 'parent_view_hostel.html', {'data': data})
@login_required(login_url='Login')
def parent_view_attendance(request):
    data = attendance.objects.all()
    return render(request, 'parent_view_attendance.html', {'data': data})
@login_required(login_url='Login')
def parent_view_staff(request):
    data = staff.objects.all()
    return render(request, 'parent_view_staff.html', {'data': data})
@login_required(login_url='Login')
def parent_view_fee(request):
    data = fee.objects.all()
    return render(request, 'parent_view_fee.html', {'data': data})
@login_required(login_url='Login')
def parent_view_room(request):
    data = room.objects.all()
    return render(request, 'parent_view_room.html', {'data': data})
@login_required(login_url='Login')
def parent_view_pay(request):
    data=payment.objects.all()
    return render(request,'parent_view_pay.html',{'data':data} )
@login_required(login_url='Login')
def delete_profile_parent(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request,'Your Account Deleted Successfully')
        return redirect('index')
    return render(request,'parent_delete_account.html')