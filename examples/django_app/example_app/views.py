from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model
    )
from django.views import generic
from django.views.generic import View
from .forms import UserForm

class ChatterBotAppView(TemplateView):
    template_name = "app.html"

class UserFormView(View):
    form_class = UserForm
    template_name = 'user_registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form':form})

class AboutView(View):
    template_name = "about.html"
    def get(self, request):
        return render(request, self.template_name)
# class UserLoginView(View):
#     form_class = UserLoginForm
#     template_name = 'login.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('/')
#                 else:
#                     print ("not active")
#             else:
#                 print ("None")
#         else:
#             print ("Form not Valid")
#
#         return render(request, self.template_name, {'form':form})
