from django.shortcuts import render
from .forms import UserRegistration
from .models import User


def add_show(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['firstname']
            lname = fm.cleaned_data['lastname']
            em = fm.cleaned_data['email']
            con = fm.cleaned_data['contact']
            pw = fm.cleaned_data['password']
            reg = User(firstname=fname, lastname=lname, email=em, contact=con, password=pw)
            reg.save()
            fm = UserRegistration()
    else:
         fm = UserRegistration()
    show = User.objects.all()
    return render(request, 'register/add_show.html', {'form': fm, 'disp':show})