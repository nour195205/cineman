
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout  
from django.contrib import messages
from django.contrib.auth.decorators import login_required  
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/films/')  # غير "home" حسب وجهتك بعد تسجيل الدخول
        else:
            return render(request, 'sign_pages/signin.html', {'error': 'Invalid credentials'})
    return render(request, 'sign_pages/signin.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'sign_pages/signup.html', {'error': 'Passwords do not match.'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'sign_pages/signup.html', {'error': 'Username already taken.'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'sign_pages/signup.html', {'error': 'Email already registered.'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('films')
    
    return render(request, 'sign_pages/signup.html')


def logout(request):
    auth_logout  (request)
    return redirect('signin')