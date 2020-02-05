from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from .validators import validar_clave

# Create your models here.

class seguridad(models.Model):

	correo=models.CharField(max_length=200, validators=[RegexValidator(regex=r'^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$')])
	clave=models.CharField(max_length=20, validators=[validar_clave])


	def __str__(self):

		return self.correo+ ': ' + self.password[::-1]


