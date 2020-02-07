from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from .validators import validar_clave, validar_correo

# Create your models here.

class seguridad(models.Model):

	correo = models.CharField(max_length=200, validators=[validar_correo])
	clave = models.CharField(max_length=16, validators=[validar_clave])


	def __str__(self):
		return self.correo + ': ' + self.clave[::-1]


