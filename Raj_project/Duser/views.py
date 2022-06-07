from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import OpsUser,File
# Create your views here.
def Signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        userForm = CreateUserForm()
        if request.method == 'POST':
            print('yes post method')
            userForm = CreateUserForm(request.POST)
            print(userForm.is_valid())
            if userForm.is_valid():
                print('yes is valid')
                userForm.save()
                user = userForm.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        dict={
            'userform':userForm
        }
        return render(request, 'signup.html',dict)

def Login(request):
    print('login')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    allfile = File.objects.all()
    dict = {
        'data':allfile
    }
    return render(request, 'home.html', dict)

def Logout(request):
    logout(request)
    return redirect('login')

def uLogout(request):
    del request.session['user']
    return redirect('opslogin')

def opsLogin(request):
    if request.method=='POST':
        print('yes clicked')
        username = request.POST.get('username')
        password = request.POST.get('password')
        match = OpsUser.objects.filter(username=username, password=password)
        print(match)
        if match:
            print('match')
            request.session['user']=username
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'opslogin.html')

def dashboard(request):
    if not request.session.get('user'):
        return redirect('opslogin')
    if request.method=='POST':
        file = request.FILES.get('file')
        user1= request.session.get('user')
        user= OpsUser.objects.get(username=user1)
        print(file)
        upload=File.objects.create(user=user, file=file)
        if upload:
            print('file uploaded successfully')
            messages.info(request, 'File Uploaded Successfully!')
        else:
            messages.info(request, 'Something went wrong!')
    print('dashboard')
    return render(request, 'dashboard.html')