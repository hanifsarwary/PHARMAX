from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import CustomUser
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import hashers
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

class loginView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('Inventory:inventoryView', kwargs={'username': request.user.username}))
        else:
            return render(request,'login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            print("i am here")
            login(request, user)
            return HttpResponseRedirect(reverse('Inventory:billView',kwargs={'username':username}))
        else:
            return render(request, 'login.html')




