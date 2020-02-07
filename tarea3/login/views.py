from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import seguridad
from .funciones import registrarUsuario, ingresarUsuario
# Create your views here.

def index(request):
	template= loader.get_template('login/login.html')
	contexto={}
	return HttpResponse(template.render(contexto, request))

def home(request, correo):
	template= loader.get_template('login/home.html')
	contexto={
	'email': correo,
	}
	return HttpResponse(template.render(contexto, request))

# Atentifica los correos
def autentificar(request):
	try:
		correo = request.GET['correo']
		contrasena = request.GET['contrasena']
		existe, data = ingresarUsuario(correo, contrasena)
	# Cuando no se introdujo bien el correo lanza error
	except KeyError:
		texto = { 'error_message': "Vuelva a intentar"}
		return render(request, 'login/login.html', texto)
	else: 
		if existe:
			template= loader.get_template('login/home.html')
			contexto={
				'email': data,
			}
			return HttpResponse(template.render(contexto,request))
		else:
			texto = { 'error_message': "el usuario no es valido"}
			return render(request, 'login/login.html')

# Registro para los usuarios
def register(request):
	template = loader.get_template('login/register.html')
	contexto={}
	return HttpResponse(template.render(contexto,request))

# Registro de usuario
def register_usuario(request):
	try:
		correo = request.POST['correo']
		contrasena = request.POST['contrasena']
		contrasena2= request.POST['contrasena2']

	except KeyError:
		texto = { 'error_message': "Vuelva a intentar"}
		return render(request, 'login/register.html', contexto)
		# validaciones como que ajuro entre al correo
		# Busca al usurio enn la bd
	# Cuando no se introdujo bien el correo lanza error
	else:
		template = loader.get_template('login/home.html')
		contexto = {

			'email' : correo,
		}
		return HttpResponse(template.render(contexto,request))



	
