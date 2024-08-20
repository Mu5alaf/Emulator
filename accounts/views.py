from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import signup_form,Login_Form,Profile_form,User_form
from .models import Profile
from django.contrib import messages
# Create your views here.


#user signup
def signup_view(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"You Have been Successfully Signed")
            return redirect('home:home_page')
        else:
            messages.error(request,"Something went wrong")
            return redirect('accounts:signup_page')
    else:
        form = signup_form()
    return render (request,'registration/signup.html',{'form':form})

#user profile
@login_required
def profile_view(request):
    user = Profile.objects.get(user=request.user)
    if request.user.is_authenticated:
        return render(request,'accounts/profile.html',{'user':user})
    else:
        return render(request,'registration/login.html')
    
#user profile edit
@login_required
def edit_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = User_form(request.POST,instance=request.user)
        profile_form = Profile_form(request.POST,request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_profile = profile_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            messages.success(request,"Your Profile Have been Successfully Updated")
            return redirect('accounts:profile')
        else:
            messages.error(request,"Something went wrong")
            return redirect('accounts:profile_edit')
    else:
        user_form = User_form(instance=request.user)
        profile_form = Profile_form(instance=profile)
        context = {'user_form':user_form,'profile_form':profile_form}
    return render(request,'accounts/edit_profile.html',context)


