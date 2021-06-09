from django.shortcuts import render
from .models import hod_table

# Create your views here.

def save(request):
    if request.method == "POST":

        reg_name = request.POST.get('id')
        photo = request.FILES.get('photo', False)
        name = request.POST.get('name')
        department = request.POST.get('dep')
        age = request.POST.get('age')
        dob = request.POST.get('sec')
        mail = request.POST.get('em')
        ph = request.POST.get('ph')
        original_data = hod_table.objects.get(REGNAME=reg_name)



        if photo == False:
            photo = original_data.PROFILE

        #SELECT * FROM hod_table WHERE REGNAME = reg_name

        datasave = hod_table.objects.get(REGNAME=reg_name)

        datasave.NAME = name
        datasave.DEPARTMENT = department
        datasave.AGE = age
        datasave.DOB = dob
        datasave.MAIL = mail
        datasave.PHONE = ph
        datasave.PROFILE = photo

        datasave.save()


    return render(request, 'loginpage2.html', context={})
