from django.shortcuts import render, HttpResponseRedirect
from .models import User

# Create your views here.

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        
        existing_user = User.objects.filter(email = email).first()
         
        if existing_user:
            return render(request, 'myapp/user_exists.html')
        new_user = User(username = username, email=email, password = password,image = image)
        new_user.save()
        
        return HttpResponseRedirect('myapp/success/')
    return render(request,'myapp/registration.html')

def success(request):
    return render(request,'myapp/success.html')

def user_exists(request):
    return render(request, 'myapp/user_exists.html')

def master(request):
    return render(request,'myapp/master.html')

def display(request):
    users = User.objects.all()
    return render(request,'myapp/display.html', {'users': users})






