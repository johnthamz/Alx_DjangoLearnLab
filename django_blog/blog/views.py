from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

# -------------------------
# Custom registration form
# -------------------------
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# -------------------------
# Registration view
# -------------------------
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

# -------------------------
# Login view
# -------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")
        else:
            messages.error(request, "Login failed. Please check username and password.")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

# -------------------------
# Logout view
# -------------------------
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("home")

# -------------------------
# Profile view with edit
# -------------------------
@login_required
def profile_view(request):
    if request.method == "POST":
        # Allow the user to update their username and email
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Failed to update profile. Please correct the errors.")
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})

