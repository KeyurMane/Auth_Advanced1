from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def homeview(request):
    return render(request,'app1/home.html')

def loginview(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pw')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid credential')
    temp_nm = 'app1/login.html'
    return render(request,temp_nm)

def logoutview(request):
    logout(request)
    return redirect('login')

def registerview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    temp_nm = 'app1/register.html'
    context = {'form':form}
    return render(request,temp_nm,context)

def change_passwordview(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changep')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app1/change_password.html', {
        'form': form
    })
