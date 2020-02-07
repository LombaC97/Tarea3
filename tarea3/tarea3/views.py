from django.shortcuts import redirect

# Para que el servidor comience en login
def redirect_view(request):
    response = redirect('login/')
    return response