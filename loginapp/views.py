from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import datetime
import bcrypt


def homepage(request):
    if 'userid' in request.session:
        return redirect('/success')
    return render(request, "index.html")


def logout(request):
    del request.session['userid']
    return redirect('/')


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                            birthday=request.POST['birthday'], password=pw_hash, email=request.POST['email'])
        request.session['userid'] = request.POST['email']
    return redirect('/success')


def success(request):
    if not 'userid' in request.session:
        return redirect('/')
    else:
        loggeduser = User.objects.get(email=request.session['userid'])
        context = {
            "user": loggeduser
        }
    return render(request, "success.html", context)


def login(request):
    login_errors = User.objects.login_validator(request.POST)
    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value)
        return redirect('/')
    if 'userid' in request.session:
        return redirect('/success')
    checkuser = User.objects.filter(email=request.POST['email'])
    if checkuser:
        loggeduser = checkuser[0]
        if bcrypt.checkpw(request.POST['password'].encode(), loggeduser.password.encode()):
            request.session['userid'] = request.POST['email']
            return redirect('/success')
    return redirect('/')
