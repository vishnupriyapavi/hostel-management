from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mainapp.forms import loginregister, student_form, parent_form


# Create your views here.

def index(request):
    return render(request,'index.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('admin1')
        elif user is not None and  user.is_student:
            if user.student.approval_status==True:
                login(request,user)
                return redirect('student')
            else:
                messages.info(request, 'user not approved')
        elif user is not None and user.is_parent:
            if user.parent.approval_status==True:
                login(request,user)
                return redirect('parents')
            else:
                messages.info(request, 'user not approved')
        else:
            messages.info(request,'Invalid password or username')

    return render(request, 'login.html')


@login_required(login_url='Login')
def admin1(request):
    return render(request,'admin.html')

@login_required(login_url='Login')
def student(request):
    return render(request, 'student_page.html')

@login_required(login_url='Login')
def parents(request):
    return render(request, 'parent_page.html')

def reg_stu(request):
    u_form=loginregister()
    s_form=student_form()
    if request.method=='POST':
        u_form=loginregister(request.POST)
        s_form=student_form(request.POST,request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user=u_form.save(commit=False)
            user.is_student=True
            user.save()
            student=s_form.save(commit=False)
            student.user=user
            student.save()
            messages.info(request,'Student register successfully')
            return redirect('Login')
    return render(request,'stu_reg.html',{'s_form':s_form,'u_form':u_form})

def par_reg(request):
    u_form=loginregister()
    p_form=parent_form()
    if request.method=='POST':
        u_form=loginregister(request.POST)
        p_form=parent_form(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user=u_form.save(commit=False)
            user.is_parent=True
            user.save()
            parent=p_form.save(commit=False)
            parent.user=user
            parent.save()
            messages.info(request, 'Parent register successfully')
            return redirect('Login')
    return render(request,'register.html',{'p_form':p_form,'u_form':u_form})


def logout_view(request):
    logout(request)
    return redirect('index')
