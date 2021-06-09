from django.shortcuts import render, redirect
from login.models import account
from login.forms import acc_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from hoddata.models import hod_table
from stddata.models import student_table
from techdata.models import teacher_table

# Create your views here.


def a(request):
    au = request.user
    if au.is_authenticated:
        return redirect('/gallary2/')

    context = {

    }
    return render(request, 'loginpage.html', context)

def e(request):
    context = {

    }
    return render(request, 'loginpage2.html', context)


def b(request):
    context = {

    }

    au = request.user
    if au.is_authenticated:
        return redirect('/gallary2/')

    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")

        form = acc_form(request.POST)
        if user != '' and user is not None:
            if password != '' and password is not None:
                if form.is_valid():
                    acc = authenticate(username=user, password=password)
                    if acc:
                        login(request,acc)
                        return redirect('/gallary2/')
                else:
                    messages.warning(request,"Invalid Username and password")
            else:
                messages.warning(request, "enter your password")
        else:
            messages.warning(request, "enter your username")
    else:
        form = acc_form()

    context['login_form'] = form
    return render(request,'loginpage.html',context)

def logout_view(request):

    logout(request)
    return redirect('mainpage')


def c(request):

    context = {

    }
    return render(request, 'new.html', context)


def register(request):

    if request.method == "POST":
        NAME = request.POST.get('name')
        EMAIL = request.POST.get('em')
        DOB = request.POST.get('sec')
        AGE = request.POST.get('age')
        PHONENO= request.POST.get('ph')
        ADDRESS = request.POST.get('add')
        USERNAME = request.POST.get('uname')
        PASSWORD = request.POST.get('password')
        CONFIRMPASSWORD = request.POST.get('cpassword')

        designation = request.POST.get('te')

        print(NAME)
        print(EMAIL)
        print(DOB)
        print(AGE)
        print(PHONENO)
        print(ADDRESS)
        print(USERNAME)
        print(PASSWORD)
        print(CONFIRMPASSWORD)
        print(designation)

        is_teacher = False
        is_student = False
        is_hod = False

        if designation == "teacher":
            is_teacher = True
        elif designation == "student":
            is_student = True
        elif designation == "hod":
            is_hod = True

        user = account.objects.create_user(username = USERNAME, password = CONFIRMPASSWORD, NAME = NAME, EMAIL = EMAIL, DOB = DOB, AGE= AGE,PHONE_NUMBER = PHONENO,
                                        ADDRESS = ADDRESS, is_teacher = is_teacher, is_student = is_student, is_hod = is_hod)
        user.save()
        reg_id = "RA1234"+USERNAME+"56789"
        if is_hod:
            hod_save = hod_table(REGNAME=reg_id,NAME=NAME,AGE=AGE,DOB=DOB,MAIL=EMAIL,PHONE=PHONENO)
            hod_save.save()
        elif is_student:
            student_save = student_table(REGNAME=reg_id,NAME=NAME,AGE=AGE,DOB=DOB,MAIL=EMAIL,PHONE=PHONENO)
            student_save.save()
        elif is_teacher:
            teacher_save = teacher_table(REGNAME=reg_id,NAME=NAME,AGE=AGE,DOB=DOB,MAIL=EMAIL,PHONE=PHONENO)
            teacher_save.save()

        return redirect('mainpage')
    else:
        context = {

        }
        return render(request, 'loginpage.html', context)


def sd(request):
    USER = request.user
    reg_id = "RA1234" + str(USER) + "56789"
    student_data = student_table.objects.get(REGNAME=reg_id)
    date_given = str(student_data.DOB)
    context = {

        "data_student": student_data,
        "DOB": date_given

    }
    return render(request, 'student.html', context)

def td(request):
    USER = request.user
    reg_id = "RA1234" + str(USER) + "56789"
    teacher_data = teacher_table.objects.get(REGNAME=reg_id)
    date_give = str(teacher_data.DOB)
    context = {

        "data_teacher": teacher_data,
        "DOB": date_give

    }
    return render(request, 'teacher.html', context)

def hd(request):
    USER = request.user
    reg_id = "RA1234"+str(USER)+"56789"
    hod_data = hod_table.objects.get(REGNAME=reg_id)
    date_given = str(hod_data.DOB)
    context = {

        "data_hod": hod_data,
        "DOB": date_given

    }
    return render(request, 'hod.html', context)
