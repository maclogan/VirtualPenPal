from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render
from .forms import UserLoginForm

# Create your views here.
def login_view(request):
    title="Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return(request, "form.html", {"form":form, "title":title})

def logout_view(request):
    return(request, "form.html", {})

def register_view(request):
    return(request, "form.html", {})
