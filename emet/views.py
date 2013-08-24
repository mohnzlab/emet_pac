from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from emet.forms import ActasPresidentesForm, ActasDiputadosForm, ActasAlcaldesForm
from django.utils import simplejson
from emet.models import RepPresidentes, Movimientos, ActasPresidentes, ActasAlcaldes, RepAlcaldes, RepDiputados, ActasDiputados
from datetime import datetime

def home(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/main/')
	else:
		formulario = AuthenticationForm()
		return render_to_response('home.html', {'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
	if request.is_ajax():
		if not request.user.is_anonymous():
			# return HttpResponseRedirect('/main/')
			respuesta = {'codigo': 1, 'msg': 'Redireccionar'}
			return HttpResponse(simplejson.dumps(respuesta))
		if request.method=='POST':
			formulario = AuthenticationForm(request.POST)
			if formulario.is_valid:
				usuario = request.POST['username']
				clave = request.POST['password']
				acceso = authenticate(username=usuario, password=clave)
				if acceso is not None:
					if acceso.is_active:
						login(request, acceso)
						respuesta = {'codigo': 1, 'msg': 'Bienvenido, redirecionar'}
						return HttpResponse(simplejson.dumps(respuesta))
						# return HttpResponseRedirect('/')
					else:
						respuesta = {'codigo': 2, 'msg': 'Este usuario no tiene permisos para acceder'}
						return HttpResponse(simplejson.dumps(respuesta))
						# return render_to_response('noactivo.html', context_instance=RequestContext(request))
				else:
					respuesta = {'codigo': 3, 'msg': 'Error de usuario y/o contrasena'}
					return HttpResponse(simplejson.dumps(respuesta))
					# return render_to_response('nousuario.html', context_instance=RequestContext(request))
		else:
			formulario = AuthenticationForm()
			return render_to_response('home.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def main(request):
	return render_to_response('main.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def mainAlcaldes(request):
	formi = ActasAlcaldes()
	AllAlcaldes = RepAlcaldes.objects.all().select_related('Movimientos').order_by('OrdenRepAlcaldes')
	return render_to_response('mainAlcaldes.html', {'TAlcaldes' : AllAlcaldes, 'formi' : formi}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def mainPresidentes(request):
	formi = ActasPresidentesForm()
	AllPresidentes = RepPresidentes.objects.all().select_related('Movimientos').order_by('OrdenRepPresidentes')
	return render_to_response('mainPresidentes.html', {'TPresidentes' : AllPresidentes, 'formi' : formi}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def mainDiputados(request):
	formi = ActasDiputadosForm()
	AllDiputados = RepDiputados.objects.all().select_related('Movimientos').order_by('OrdenRepDiputados')
	return render_to_response('mainDiputados.html', {'TDiputados' : AllDiputados, 'formi' : formi}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def salir(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def ActaPresidenteAdd(request):
	if request.is_ajax():
		if request.method == 'POST':
			NumActaCount = ActasPresidentes.objects.filter(NoActa=request.POST['NoActa'], RepPresidenteID=request.POST['RepPresidenteID']).count()
			if NumActaCount < 1:
				formi = ActasPresidentesForm(data=request.POST)
				if formi.is_valid():
					u = formi.save(commit=False)
					u.FechaRegistro = datetime.now()
					u.save()
					respuesta = {'codigo': 1, 'msg': 'El acta ha sido guardada'}
					return HttpResponse(simplejson.dumps(respuesta))
				else:
					respuesta = {'codigo': 2, 'msg': 'No se ha podido guardar el acta '}
					return HttpResponse(simplejson.dumps(respuesta))
			else:
				respuesta = {'codigo': 3, 'msg': 'ERROR, esta acta ya habia sido guardada.'}
				return HttpResponse(simplejson.dumps(respuesta))

@login_required(login_url='/login/')
def ActaDiputadoAdd(request):
	pass

@login_required(login_url='/login/')
def ActaAlcaldeAdd(request):
	if request.is_ajax():
		if request.method == 'POST':
			NumActaCount = ActasAlcaldes.objects.filter(NoActa=request.POST['NoActa'], RepAlcaldeID=request.POST['RepAlcaldeID']).count()
			if NumActaCount < 1:
				formi = ActasAlcaldesForm(data=request.POST)
				if formi.is_valid():
					u = formi.save(commit=False)
					u.FechaRegistro = datetime.now()
					u.save()
					respuesta = {'codigo': 1, 'msg': 'El acta ha sido guardada'}
					return HttpResponse(simplejson.dumps(respuesta))
				else:
					respuesta = {'codigo': 2, 'msg': 'No se ha podido guardar el acta '}
					return HttpResponse(simplejson.dumps(respuesta))
			else:
				respuesta = {'codigo': 3, 'msg': 'ERROR, esta acta ya habia sido guardada.'}
				return HttpResponse(simplejson.dumps(respuesta))