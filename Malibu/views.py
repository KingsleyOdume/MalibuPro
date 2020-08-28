from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong entering')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':  # first code
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        username = request.POST['username']
        date_joined = request.POST['date_joined']
        id = request.POST['id']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:  # checking for password match
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Name is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    password=password1, email=email, username=username, first_name=FirstName,
                    last_name=LastName, date_joined=date_joined, id=id)
                user.save()
                messages.success(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')  # checking for password match
            return redirect('register')
        return redirect('home')
    else:
        return render(request, 'register.html')  # part of first code

