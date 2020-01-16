from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Event,Event_Member,Member 
from .codeUtility import CodeUtility
# Create your views here.
def index(request):
	return render(request,'index.html')
def serveLoggedIn(username):
	
	responsePage=""

	responsePage+="<!Doctype html>"
	responsePage+="<html>"
	responsePage+="<head><title>Event Management | HOME</title>"
	responsePage+="<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css\">"
	responsePage+="<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js\"></script>"
	responsePage+="<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js\"></script>"
	responsePage+="<style>"
	responsePage+="#header"
	responsePage+="{"
	responsePage+="padding:10px;"
	responsePage+="height:100px;"
	responsePage+="margin-bottom:0px;"
	responsePage+="background-color:#e6e6e6;"
	responsePage+="}"
	responsePage+=".opb"
	responsePage+="{"
	responsePage+="width:70%;"
	responsePage+="//text-align:left;"
	responsePage+="}"
	responsePage+="#usernameSpan"
	responsePage+="{"
	responsePage+="color:#0099cc;"
	responsePage+="font-weight:bold;"
	responsePage+="}"
	responsePage+=""
	responsePage+="#main-container"
	responsePage+="{"
	responsePage+="width:100%;"
	responsePage+="margin-top:0px;"
	responsePage+="padding:20px;"
	responsePage+="//background:url('/static/homeBackground.jpg') 100% 0 no-repeat fixed;"
	responsePage+="height:900px;"
	responsePage+="}"
	responsePage+=".sub-container"
	responsePage+="{"
	responsePage+="border:1px solid #e6e6e6;"
	responsePage+="padding:10px;"
	responsePage+="margin-right:50px;"
	responsePage+="background:rgba(255,255,255,0.6);"
	responsePage+="border-radius:8px;"
	responsePage+="box-shadow:2px 2px 12px black;"
	responsePage+="width:300px;"
	responsePage+="}"
	responsePage+=".row-element"
	responsePage+="{"
	responsePage+="display:-webkit-box;"
	responsePage+="display:moz box;"
	responsePage+="display:ms flexbox;"
	responsePage+="display:flexbox;"
	responsePage+=""
	responsePage+="flex-direction:row;"
	responsePage+="flex-align:start;"
	responsePage+="}"
	responsePage+=".first-column-element"
	responsePage+="{"
	responsePage+="-webkit-box-ordinal-group:1;"
	responsePage+="moz box ordinal group:1;"
	responsePage+="ms flex order:1;"
	responsePage+="webkit order:1;"
	responsePage+="}"
	responsePage+=".second-column-element"
	responsePage+="{"
	responsePage+="-webkit-box-ordinal-group:2;"
	responsePage+="moz box ordinal group:2;"
	responsePage+="ms flex order:2;"
	responsePage+="webkit order:2;"
	responsePage+="}"
	responsePage+=".third-column-element"
	responsePage+="{"
	responsePage+="-webkit-box-ordinal-group:3;"
	responsePage+="moz box ordinal group:3;"
	responsePage+="ms flex order:3;"
	responsePage+="webkit order:3;"
	responsePage+="}"
	responsePage+=".fourth-column-element"
	responsePage+="{"
	responsePage+="-webkit-box-ordinal-group:4;"
	responsePage+="moz box ordinal group:4;"
	responsePage+="ms flex order:4;"
	responsePage+="webkit order:4;"
	responsePage+="}"
	responsePage+="</style>"
	responsePage+="<script>"
	responsePage+="function show(pre)"
	responsePage+="{"
	responsePage+="var k=document.getElementsByClassName(\"eventDiv\");"
	responsePage+="k[0].style.display=\"none\";"
	responsePage+="k[1].style.display=\"none\";"
	responsePage+="k[2].style.display=\"none\";"
	responsePage+="document.getElementById(pre+\"EventDiv\").style.display=\"block\";"
	responsePage+="}"
	responsePage+="</script>"
	responsePage+="</head>"
	responsePage+="<body>"
	responsePage+="<div id='header'>"
	responsePage+="<center><h1 id='title'>Event Management System</h1></center>"
	responsePage+="<span id='usernameSpan'>nileshtest124@gmail.com</span>"
	responsePage+="<a href='/eventManagement'><button id='logout' class='btn btn-danger' style='float:right;margin-right:50px;margin-bottom:70px;'>Logout</button></a>"
	responsePage+=""
	responsePage+="</div>"
	responsePage+=""
	responsePage+="<div id='main-container' >"
	responsePage+="<a href='/eventManagement/addEvent?code='><button id='addEvent' class='btn btn-success' style=';margin-right:10px;'>AddEvent</button></a><br/></br>"
	responsePage+=""
	responsePage+="<button class='opb btn btn-primary' onclick='show(\"public\")'>Show Public Events</button><br/></br>"
	responsePage+="<div id='publicEventDiv' class='eventDiv' style='display:none'>"
	responsePage+="Here Public Events will be displayed."
	responsePage+="</div>"
	responsePage+="<button  class='opb btn btn-info' onclick='show(\"my\")'>Show My Events</button><br/></br>"
	responsePage+="<div id='myEventDiv' class='eventDiv' style='display:none'>"
	responsePage+="Here Events, created by user will be displayed."
	responsePage+="</div>"
	responsePage+=""
	responsePage+="<button class='opb btn btn-secondary' onclick='show(\"joined\")' >Show Joined Events</button><br/></br>"
	responsePage+="<div id='joinedEventDiv' class='eventDiv' style='display:none'>"
	responsePage+="Here Events, joined by user will be displayed."
	responsePage+="</div>"
	responsePage+=""
	responsePage+="</div>"
	responsePage+="</body>"
	responsePage+="</html>"



	return responsePage

def login(request):
	data=request.POST
	username=data.get('username')
	password=data.get('password')
	listOfMembers=Member.objects.all()
	for member in listOfMembers:
		if(member.username==username and member.password_key==password):
			return HttpResponse(serveLoggedIn(username));
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