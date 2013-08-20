from django import forms
from django.forms import ModelForm
from emet.models import ActasPresidentes, ActasDiputados, ActasAlcaldes
from datetime import datetime

class ActasPresidentesForm(ModelForm):
	class Meta:
		model = ActasPresidentes

class ActasDiputadosForm(ModelForm):
	class Meta:
		model = ActasDiputados

class ActasAlcaldesForm(ModelForm):
	class Meta:
		model = ActasAlcaldes
