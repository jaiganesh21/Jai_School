from django.shortcuts import render
from .models import student_table


# Create your views here.

def saveas(request):
    if request.method == "POST":
        reg_name = request.POST.get('id')
        photo = request.FILES.get('photo', False)
        name = request.POST.get('name')
        CLASS = request.POST.get('class')
        age = request.POST.get('age')
        dob = request.POST.get('sec')
        mail = request.POST.get('em')
        ph = request.POST.get('ph')
        teacher_id = request.POST.get('tec')
        original_data = student_table.objects.get(REGNAME=reg_name)

        # print(reg_name)

        if photo == False:
            # photo = "user.png"
            photo = original_data.PROFILE


        datasave = student_table.objects.get(REGNAME=reg_name)

        datasave.NAME = name
        datasave.CLASS = CLASS
        datasave.AGE = age
        datasave.DOB = dob
        datasave.MAIL = mail
        datasave.PHONE = ph
        datasave.TEACHER_ID = teacher_id
        datasave.PROFILE = photo

        datasave.save()

    return render(request, 'loginpage2.html', context={})
