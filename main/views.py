from django.shortcuts import render, redirect, get_object_or_404
from main.models import SignUp
from main.forms import SignUpForm
import datetime

# Create your views here.
def main(request):
    template = 'main/main.html'
    return render(request, template, {'form':SignUpForm()})


def addSignUp(request):
    template = 'main/main.html'
    form = SignUpForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save()
    return success(request)


def success(request):
    return render(request, 'main/success.html')


def signUp(request, signUpID):
    template = 'main/main2.html'
    signUp = get_object_or_404(SignUp, id=signUpID)
    if request.method=='GET':
        form = SignUpForm(instance=signUp)
        return render(request, template, {'form':form, 'signUp':signUp})
    #POST 
    form = SignUpForm(request.POST, instance=signUp)
    if not form.is_valid():
        return render(request, template, {'form':form,'signUp':signUp})
    form.save()
    return admin7123(request)


def admin7123(request):
    SignUps = SignUp.objects.all()
    context = {'SignUps':SignUps}
    return render(request, 'main/list.html', context)


def deletesignUp(request, signUpID):
    if request.method=='GET':
        return admin7123(request)
    # POST
    signUp = get_object_or_404(SignUp, id=signUpID)
    signUp.delete()
    return admin7123(request)