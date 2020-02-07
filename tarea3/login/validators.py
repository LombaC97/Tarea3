import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Datos permitidos en el correo
regexCorreo = '^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$'

# Se valida que el correo sea valido
def validar_correo(value):
	acepto = re.search(regexCorreo, value)
	if(not acepto):
		raise ValidationError(_('%(value)s correo invalido'), params={'value': value},)

# Verifia si la contrasena es correcto
def validar_clave(value):
	if(not len(value) <= 8 and len(value) >= 16 ):
		raise ValidationError(_('%(value)s contrasena invalida'), params={'value': value},)

# Verifica si las contrasenas son iguales
def validar_iguales(value1, value2):
	igual = (value1 == value2)
	if(not igual):
		raise ValidationError(_('%(value2)s no coinciden las contrasenas'), params={'value1': value1, 'value2': value2},)



