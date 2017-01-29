from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner!")

def about(requet):
	link = "Rango says here is the about page" + '<a href = "/rango">Main Page</a>'
	return HttpResponse(link)