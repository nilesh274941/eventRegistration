from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Event,Event_Member,Member 
from .codeUtility import CodeUtility
# Create your views here.
def index(request):
	return render(request,'index.html')
def login(request):
	data=request.POST
	username=data.get('username')
	password=data.get('password')
	listOfMembers=Member.objects.all()
	for member in listOfMembers:
		if(member.username==username and member.password_key==password):
			return HttpResponse("logged in.");
	return render(request,'loginError.html');
def register(request):
	data=request.POST
	username=data.get('username')
	password=data.get('password')
	name=data.get('name')
	listOfMembers=Member.objects.all()
	for member in listOfMembers:
		if(member.username==username): return render(request,'registerError.html');
	code=CodeUtility.getMemberCode()
	newMember=Member(name=name,password_key=password,username=username,code=code)
	newMember.save()
	return HttpResponse('User Registered.')