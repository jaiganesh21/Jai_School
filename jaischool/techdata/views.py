from django.shortcuts import render
from .models import teacher_table


# Create your views here.

def saves(request):
    if request.method == "POST":
        reg_name = request.POST.get('id')
        photo = request.FILES.get('photo', False)
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('sec')
        mail = request.POST.get('em')
        hod_id = request.POST.get('Hod')
        ph = request.POST.get('ph')
        original_data = teacher_table.objects.get(REGNAME=reg_name)

        if photo == False:
            # photo = "user.png"
            photo = original_data.PROFILE


        datasave = teacher_table.objects.get(REGNAME=reg_name)

        datasave.NAME = name
        datasave.AGE = age
        datasave.DOB = dob
        datasave.MAIL = mail
        datasave.PHONE = ph
        datasave.HOD_ID = hod_id
        datasave.PROFILE = photo

        datasave.save()


    return render(request, 'loginpage2.html', context={})
