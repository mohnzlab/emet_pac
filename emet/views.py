# -*- encoding: utf-8 -*-
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
from django.core import serializers
from django.db.models import Count, Min, Sum, Avg

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
	AllDiputados = ''
	#AllDiputados = RepDiputados.objects.all().select_related('Movimientos').order_by('OrdenRepDiputados')
	AllMovimientos = Movimientos.objects.all().order_by('MovimientoNombre')
	return render_to_response('mainDiputados.html', {'TDiputados' : AllDiputados, 'TMovimientos' : AllMovimientos}, context_instance=RequestContext(request))

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

@login_required(login_url='/login/')
def ActaDiputadoAdd(request):
	if request.is_ajax():
		if request.method == 'POST':
			NumActaCount = ActasDiputados.objects.filter(NoActa=request.POST['NoActa'], RepDiputadoID=request.POST['RepDiputadoID']).count()
			if NumActaCount < 1:
				formi = ActasDiputadosForm(data=request.POST)
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
def FiltrarDiputados(request):
	if request.is_ajax():
		q = request.GET.get('q', False)
		if q is not None:           
			AllDiputados = RepDiputados.objects.filter(MovimientoID = q).order_by('OrdenRepDiputados')
			return render_to_response('diputadosFiltrados.html', {'TDiputados' : AllDiputados}, context_instance=RequestContext(request))

def MostrarResultadosAlcaldesGrafica(request):
	if request.is_ajax():
		ResultadosAlcaldes = RepAlcaldes.objects.annotate(SumaValidos=Sum('actasalcaldes__VotosValidos'), SumaBlancos=Sum('actasalcaldes__VotosBlancos'), SumaNulos=Sum('actasalcaldes__VotosNulos'))
	else:
		ResultadosAlcaldes = RepAlcaldes.objects.annotate(SumaValidos=Sum('actasalcaldes__VotosValidos'), SumaBlancos=Sum('actasalcaldes__VotosBlancos'), SumaNulos=Sum('actasalcaldes__VotosNulos'))

	return render_to_response('armarResultadosAlcaldes.html', {'TAlcaldes' : ResultadosAlcaldes}, context_instance=RequestContext(request))

def Mostrar9DiputadosGanando(request):
	if request.is_ajax():
		Resultados9Diputados = RepDiputados.objects.annotate(SumaValidos=Sum('actasdiputados__CantVotos')).order_by('RepDiputadoID')
	else:
		Resultados9Diputados = RepDiputados.objects.annotate(SumaValidos=Sum('actasdiputados__CantVotos')).order_by('RepDiputadoID')

	return render_to_response('armarResultados9Diputados.html', {'TDiputados' : Resultados9Diputados}, context_instance=RequestContext(request))

def ReportesAlcades(request):
	SumAlcalde1 = RepAlcaldes.objects.annotate(Suma=Sum('actasalcaldes__VotosValidos'))

	lista = []
	lista2 = []

	for n in SumAlcalde1:
		lista.append(n.Suma)

	for o in SumAlcalde1:
		lista2.append(o)

	return render_to_response('graficaAlcaldes.html', {'Valor' : lista, 'Nombres' : lista2}, context_instance=RequestContext(request))

def Dashboard(request):
	SumAlcalde1 = RepAlcaldes.objects.annotate(Suma=Sum('actasalcaldes__VotosValidos'))
	SumPresidentes = RepPresidentes.objects.annotate(Suma=Sum('actaspresidentes__VotosValidos')).order_by('OrdenRepPresidentes')
	SumDiputados = RepDiputados.objects.annotate(Suma=Sum('actasdiputados__CantVotos')).order_by('-Suma')[:9]

	lista = []
	lista2 = []
	lista12 = []
	lista22 = []
	lista13 = []
	lista23 = []

	for n in SumAlcalde1:
		lista.append(n.Suma)

	for o in SumAlcalde1:
		lista2.append(o)

	for a  in SumPresidentes:
		lista12.append(a.Suma)

	for b in SumPresidentes:
		lista22.append(b)

	for c in SumDiputados:
		lista13.append(c.Suma)

	for d in SumDiputados:
		lista23.append(d)

	return render_to_response('dashboard.html', {'Valor' : lista, 'Nombres' : lista2, 'Valor2' : lista12, 'Nombres2' : lista22, 'Valor3' : lista13, 'Nombres3' : lista23}, context_instance=RequestContext(request))


def DatosAlcaldes(request):
	if request.method == 'GET':
		SumAlcalde1 = RepAlcaldes.objects.annotate(Suma=Sum('actasalcaldes__VotosValidos'))
		lista = []
		for n in SumAlcalde1:
			lista.append(n.Suma)
		return HttpResponse(simplejson.dumps(lista), content_type="application/json")

def ReportesPresidentes(request):
	SumPresidentes = RepPresidentes.objects.annotate(Suma=Sum('actaspresidentes__VotosValidos')).order_by('OrdenRepPresidentes')
	
	lista = []
	lista2 = []
	
	for n in SumPresidentes:
		lista.append(n.Suma)

	for o in SumPresidentes:
		lista2.append(o)

	return render_to_response('graficaPresidentes.html', {'Valor' : lista, 'Nombres' : lista2}, context_instance=RequestContext(request))


def DatosPresidentes(request):
	if request.method == 'GET':
		SumPresidentes = RepPresidentes.objects.annotate(Suma=Sum('actaspresidentes__VotosValidos')).order_by('OrdenRepPresidentes')
		lista = []
		for n in SumPresidentes:
			lista.append(n.Suma)
		return HttpResponse(simplejson.dumps(lista), content_type="application/json")

def ReportesDiputados(request):
	SumDiputados = RepDiputados.objects.annotate(Suma=Sum('actasdiputados__CantVotos'))

	lista = []
	lista2 = []

	for n in SumDiputados:
		lista.append(n.Suma)
	
	for o in SumDiputados:
		lista2.append(o)
		
	return render_to_response('graficaDiputados.html', {'Valor' : lista, 'Nombres' : lista2}, context_instance=RequestContext(request))


def DatosDiputados(request):
	if request.method == 'GET':
		SumDiputados = RepDiputados.objects.annotate(Suma=Sum('actasdiputados__CantVotos')).order_by('-Suma')[:9]
		lista = []
		for n in SumDiputados:
			lista.append(n.Suma)
		return HttpResponse(simplejson.dumps(lista), content_type="application/json")

