from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import os
from django import forms
from django.contrib import messages
from .form import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
        
@login_required(login_url='login')
def home(request):
	return render(request,'myapp/main.html') 
	
@login_required(login_url='login')
def index(request):
	return render(request,'myapp/index.html')
	
def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	form = CreateUserForm()
	
	if request.method=='POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Account successfully created.')
			return redirect('login')
	context={'form':form}
	return render(request,'myapp/register.html',context)
	
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		messages.error(request, 'Username or password is invalid!')
	return render(request,'myapp/login.html')
		
def logoutPage(request):
	logout(request)
	return redirect('login')
		

'''@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer_delete(request,customer_id):
	customer=Customer.objects.get(id=customer_id)
	if request.method == 'POST':
		customer.delete()
		return redirect('/')
	context={'customer':customer}
	return render(request,"c1/customer_delete.html",context)
@login_required(login_url='login')

'''


