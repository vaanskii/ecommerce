from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from item.models import Category,Item
from django.contrib.auth import update_session_auth_hash,logout
from .forms import SignUpForm, UpdateProfileForm, PasswordChangeForm
from django.contrib import messages


def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:20]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def signup(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/login/', {'categories': categories})
        
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form,
        'categories': categories,
    })


@login_required
def update_profile(request):
    user = request.user
    categories = Category.objects.all()

    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, instance=user)
        password_form = PasswordChangeForm(user, request.POST)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully - Username changed')

        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully')

            # Log out the user
            logout(request)

            return redirect(reverse('core:login', {'categories': categories}))

    else:
        profile_form = UpdateProfileForm(instance=user)
        password_form = PasswordChangeForm(user)

    return render(request, 'core/update_profile.html', {'profile_form': profile_form, 'password_form': password_form})