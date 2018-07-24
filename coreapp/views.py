from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm


from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import get_object_or_404
from .models import employers


def homepage(request):
	if request.method == "POST" :
		form = UserLoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username,password=password)
			login(request,user)
			if not request.user.is_authenticated():
				errormsg = "Username/Password incorrect"
				title= "Error while trying to login"
				return render (request, 'tripod/index.html',{"title":title,"error":errormsg})
			else:
				return redirect("/add/")
		else:
			errormsg = "Username/Password incorrect"
			title="Error while trying to login"
	else:
		errormsg = ""
		title = "Add"  
	return render(request, 'tripod/index.html', {"title":title, "error":errormsg})


def createmployee(request):
	if not request.user.is_authenticated:
		return redirect("/")
	context = {}
	if request.method == "POST" :
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit = False)
			user.save()
			context = {'success': True}
		else:
			context = {'form': form}
	context.update({'title':'Create Employer'})
	return render(request, 'tripod/createuser.html', context)



def employees(request):
	if not request.user.is_authenticated:
		return redirect("/")
	allUser = employers.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(allUser, 10) # Show 10 contacts per page
	try:
		allUsers = paginator.page(page)
	except PageNotAnInteger:
		allUsers = paginator.page(1)
	except EmptyPage:
		allUsers = paginator.page(paginator.num_pages)

	context = {'users': allUsers, 'allUsers': allUser, 'title': 'List of employees'}
	return render(request, 'tripod/list.html', context)


def signout(request):
	logout(request)
	return redirect("/")