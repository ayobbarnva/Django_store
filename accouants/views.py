from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,signals
from . import forms
from .models import User
#login
def login_views(request):
            if request.user.is_authenticated:
                 return redirect('/home/')
            else:
                if request.method=='POST':
                    form=forms.LoginForm(request.POST)
                    print(form.is_valid())
                    print(form.cleaned_data if form.is_valid() else form.errors)
                    if form.is_valid():
                        phone_number=form.cleaned_data['phone_number']
                        password=form.cleaned_data['password']
                        user=authenticate(request,phone_number=phone_number,password=password)
                        if user is not None:
                            login(request,user)
                            return redirect('/home/')
                        else :                              
                           form.add_error(None, "Phone number or password is incorrect.")
                           return render(request,'login.html',context={'form':form})
                    else:
                        form.add_error(None,"phone or password is none")
                        return render(request,"login.html",context={'form':form})
                else:
                      form=forms.LoginForm()
                      return render(request,"login.html",context={'form':form})
#signup views
def sigin_views(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else: 
        if request.method=='POST':
            form=forms.SignupForm(request.POST)
            if form.is_valid():
                phone_number=form.cleaned_data['phone_number']
                password=form.cleaned_data['password']
                password_confirmation=form.cleaned_data['password_confirmation']
                if User.objects.filter(phone_number=phone_number).exists():
                      print("PHONE:", phone_number)
                      print("EXISTS:", User.objects.filter(phone_number=phone_number).exists())
                      form.add_error('phone_number','user is exists ')
                      return render(request,'register.html',context={'form':form})
                else:
                      user=User.objects.create_user(phone_number=phone_number,password=password_confirmation)
                      if user is not None:
                        login(request,user)
                        return redirect('/home/')
            else:
                 return render(request,'register.html',context={'form':form})
        else:
            form=forms.SignupForm()
            return render(request,'register.html',context={'form':form})
def logout_views(request):
     logout(request)
     return redirect('/login/')
def edit_account(request):
    if request.user.is_authenticated:
        if request.method=='POST': 
            form=forms.ProfileForm(request.POST,request.FILES,instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/home/')
            form=forms.ProfileForm(instance=request.user)
            return render(request,'edit_profile.html',context={'form':form})
        else:
            form=forms.ProfileForm(instance=request.user)
            return render(request,'edit_profile.html',context={'form':form})
    else:
         return redirect('/login/')
def show_profile(request):
     if request.user.is_authenticated:
          data=request.user
          return render(request,'my_profile.html',context={'user':data})
     else:
          return redirect('/home/')