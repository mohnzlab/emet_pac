from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from emet.forms import ActasPresidentesForm, ActasDiputadosForm, ActasAlcaldesForm
from django.utils import simplejson

def home(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/main/')
	else:
		formulario = AuthenticationForm()
		return render_to_response('home.html', {'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/main/')
	if request.method=='POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/main/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
		return render_to_response('home.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def main(request):
	return render_to_response('main.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def mainAlcaldes(request):
	return render_to_response('mainAlcaldes.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def mainPresidentes(request):
	formi = ActasPresidentesForm()

	return render_to_response('mainPresidentes.html', {'formi' : formi}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def salir(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def ActaPresidenteAdd(request):
	if request.is_ajax():
		if request.method == 'POST':
			form = ActasPresidentesForm(data=request.POST)
			if form.is_valid():
				u = form.save(commit=False)
				u.UsuarioEmetID = request.user
				u.save()

				respuesta = {'codigo': 1, 'msg': 'El acta ha sido guardada'}
				return HttpResponse(simplejson.dumps(respuesta))
			else:
				respuesta = {'codigo': 2, 'msg': 'No se ha podido guardar el acta '}
				return HttpResponse(simplejson.dumps(respuesta))

@login_required(login_url='/login/')
def ActaDiputadoAdd(request):
	if request.is_ajax():
		if request.method == 'POST':
			form = ActasDiputadosForm(data=request.POST)
			if form.is_valid():
				u = form.save(commit=False)
				user2 = request.user
				u.UsuarioEmetID = user2.pk
				u.save()

				respuesta = {'codigo': 1, 'msg': 'La ubicacion fue guardada'}
				return HttpResponse(simplejson.dumps(respuesta))
			else:
				respuesta = {'codigo': 2, 'msg': 'Faltan datos'}
				return HttpResponse(simplejson.dumps(respuesta))

@login_required(login_url='/login/')
def ActaAlcaldeAdd(request):
	if request.is_ajax():
		if request.method == 'POST':
			form = ActasAlcaldesForm(data=request.POST)
			if form.is_valid():
				u = form.save()

				respuesta = {'codigo': 1, 'msg': 'La ubicacion fue guardada'}
				return HttpResponse(simplejson.dumps(respuesta))
			else:
				respuesta = {'codigo': 2, 'msg': 'Faltan datos'}
				return HttpResponse(simplejson.dumps(respuesta))