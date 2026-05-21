from django.shortcuts import render,redirect
from .forms import RegistrationForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):
    if request.method=='POST':
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")
        
        user=authenticate(
            request,
            username=user_name,
            password=pass_word
        )

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
        
    return render(request,'login.html')


def signup(request):
    print(request)
    if request.method == 'POST':
        print(request.method)
        form=RegistrationForm(request.POST or None)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('login')

        else:
            print(form.errors)

    form=RegistrationForm()
    return render(request,'signup.html',{"form":form})

@login_required
def home(request):
    return render(request,'home.html')


def logout_page(request):
    logout(request)
    return render(request,'login.html')