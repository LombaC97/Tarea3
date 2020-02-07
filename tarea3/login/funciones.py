from .validators import validar_clave, validar_correo
from django.core.exceptions import ValidationError

def registrarUsuario(email, password, passwordconf):
    try:
        validar_correo(email)
        validar_clave(password)
        validar_clave(passwordconf)
    except ValidationError:
        return False, ValidationError
    return True, email

def ingresarUsuario(email, password):
    try:
        validar_correo(email)
        validar_clave(password)
    except ValidationError:
        return False, ValidationError
    return True, email
