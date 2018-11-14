from django.shortcuts import render,redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.utils import timezone
from .models import Formulario
from .models import rescatados


def pagina_principal(request):
	rescatado = rescatados.objects.all()
	contexto = {'rescatados':rescatado}
	return render(request,'TheRialPerris/PaginaPrincipal.html',contexto)
    
    
def pagina_formulario(request):
	form = Formulario()
	if request.method == "POST":
	    
		form.CorreoElectronico = request.POST['em']
		form.Run = request.POST['rut']
		form.Nombre = request.POST['nom']
		form.FechaNacimiento = request.POST['fec']
		form.Telefono = request.POST['telef']
		form.region = request.POST['regi']
		form.Comuna = request.POST['com']
		form.TipoCasa = request.POST['tipocasa']
		form.save()
		
    
	return render(request,'TheRialPerris/Formulario.html')


def nuevo_rescatado(request):
	form = rescatados()
	if request.method == "POST":
	    
		form.Nombreresc = request.POST['nombreresc']
		form.RazaPredom = request.POST['razaresc']
		form.Descripcion = request.POST['descripcionresc']
		form.Estado = request.POST['estadoresc']
		form.image = request.FILES['imagenresc']
		form.save()

	return render(request,'TheRialPerris/nuevorescatado.html') 








# Create your views here.
