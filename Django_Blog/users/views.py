from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserUpdateForm,ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from os import remove



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# to update profile
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        # to delete old profile images
        old_image = request.user.profile.image.path
        print(f"\nold image -- {old_image} and it's type {type(old_image)}\n")
        if old_image != 'C:\\Users\\sagar\\Desktop\\Django\\django_blog\\media\\profile_pics\\default.jpg':
            permission = 'yes'
        else:
            permission = 'no'

        if u_form.is_valid() and p_form.is_valid():
            if permission =='yes':remove(old_image)
            u_form.save()
            p_form.save()
            messages.success(request,'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {'u_form':u_form,'p_form':p_form}
    return render(request, 'users/profile.html',context)