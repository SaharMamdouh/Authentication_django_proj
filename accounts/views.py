from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def create_user(request):
    form=UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            print("form is valid")
            saved_form=form.save()
            login(request,saved_form)
        else:
            print("form is not valid")

    return render(request,'registration/signup.html',context={'form':form})
