from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import seguridad
# Create your views here.


def index(request):
	
	template= loader.get_template('login/login.html')
	contexto={}
	return HttpResponse(template.render(contexto, request))