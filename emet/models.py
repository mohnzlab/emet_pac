#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Movimientos(models.Model):
	MovimientoID = models.AutoField(primary_key=True)
	MovimientoNombre = models.CharField(max_length=100, help_text='Nombre del Movimiento', verbose_name=u'Nombre')
	MovimientoCodigo = models.CharField(max_length=50, help_text='Codigo del Movimiento', verbose_name=u'Codigo')
	FechaRegistro = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Registro', verbose_name=u'Fecha')

	def __unicode__(self):
		return self.MovimientoNombre

class RepAlcaldes(models.Model):
	RepAlcaldeID = models.AutoField(primary_key=True)
	MovimientoID = models.ForeignKey(Movimientos)
	RepAlcaldeNombre = models.CharField(max_length=100, help_text='Nombre del Candidato a Alcalde', verbose_name=u'Nombre')
	RepAlcaldeCodigo = models.CharField(max_length=10, help_text='Codigo del Candidato a Alcalde', verbose_name=u'Codigo')
	RepImagen = models.ImageField(upload_to='alcaldes', verbose_name=u'Imagen')
	FechaRegistro = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Registro', verbose_name=u'Fecha')
	OrdenRepAlcaldes = models.IntegerField(max_length=11, help_text='Orden a Mostrar', verbose_name=u'Orden')

	def __unicode__(self):
		return self.RepAlcaldeNombre

class RepDiputados(models.Model):
	RepDiputadoID = models.AutoField(primary_key=True)
	MovimientoID = models.ForeignKey(Movimientos)
	RepDiputadoNombre = models.CharField(max_length=100, help_text='Nombre del Candidato a Diputado', verbose_name=u'Nombre')
	RepDiputadoCodigo = models.CharField(max_length=50, help_text='Codigo del Candidato a Diputado', verbose_name=u'Codigo')
	RepDiputadoImagen = models.ImageField(upload_to='diputados', verbose_name=u'Imagen')
	FechaRegistro = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Registro', verbose_name=u'Fecha')
	OrdenRepDiputados = models.IntegerField(max_length=11, help_text='Orden a Mostrar', verbose_name=u'Orden')

	def __unicode__(self):
		return self.RepDiputadoNombre

class RepPresidentes(models.Model):
	RepPresidenteID = models.AutoField(primary_key=True)
	MovimientoID = models.ForeignKey(Movimientos)
	RepPresidenteNombre = models.CharField(max_length=100, help_text='Nombre del Candidato a Presidente', verbose_name=u'Nombre')
	RepPresidenteCodigo = models.CharField(max_length=50, help_text='Codigo del Candidato a Presidente', verbose_name=u'Codigo')
	RepPresidenteImagen = models.ImageField(upload_to="presidentes", verbose_name=u'Imagen')
	FechaRegistro = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Registro', verbose_name=u'Fecha')
	OrdenRepPresidentes = models.IntegerField(max_length=11, help_text='Orden a Mostrar', verbose_name=u'Ordens')

	def __unicode__(self):
		return self.RepPresidenteNombre

class ActasPresidentes(models.Model):
	ActaPresidenteID = models.AutoField(primary_key=True)
	RepPresidenteID = models.ForeignKey(RepPresidentes)
	UsuarioEmetID = models.ForeignKey(User)
	NoActa = models.CharField(max_length=10, help_text='Numero de Acta', verbose_name=u'Numero')
	VotosValidos = models.IntegerField(max_length=11, help_text='Votos Validos', verbose_name=u'Votos Validos')
	VotosBlancos = models.IntegerField(max_length=11, help_text='Votos Blancos', verbose_name=u'Votos Blancos')
	VotosNulos = models.IntegerField(max_length=11, help_text='Votos Nulos', verbose_name=u'Votos Nulos')
	FechaRegistro = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Registro', verbose_name=u'Fecha')

	def __unicode__(self):
		return self.NoActa

class ActasDiputados(models.Model):
	ActaDiputadoID = models.AutoField(primary_key=True)
	RepDiputadoID = models.ForeignKey(RepDiputados)
	UsuarioEmetID = models.ForeignKey(User)
	NoActa = models.CharField(max_length=10, help_text='Numero de Acta', verbose_name=u'Numero')
	CantVotos = models.IntegerField(max_length=11, help_text='Cantidad de Votos', verbose_name=u'Cantidad de Votos')
	FechaRegistro = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Registro', verbose_name=u'Fecha')

	def __unicode__(self):
		return self.NoActa

class ActasAlcaldes(models.Model):
	ActaAlcaldeID = models.AutoField(primary_key=True)
	RepAlcaldeID = models.ForeignKey(RepAlcaldes)
	UsuarioEmetID = models.ForeignKey(User)
	NoActa = models.CharField(max_length=10, help_text='Numero de Acta', verbose_name=u'Numero')
	VotosValidos = models.IntegerField(max_length=11, help_text='Votos Validos', verbose_name=u'Votos Validos')
	VotosBlancos = models.IntegerField(max_length=11, help_text='Votos Blancos', verbose_name=u'Votos Blancos')
	VotosNulos = models.IntegerField(max_length=11, help_text='Votos Nulos', verbose_name=u'Votos Nulos')
	FechaRegistro = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Registro', verbose_name=u'Fecha')

	def __unicode__(self):
		return self.NoActa

class Notificaciones(models.Model):
	NotificacionID = models.AutoField(primary_key=True)
	CorreoDestino = models.CharField(max_length=100, help_text='Correo de Destino', verbose_name=u'Correo')
	Mensaje = models.TextField(max_length=10000, help_text='Mensaje', verbose_name=u'Mensaje')
	FechaRegistro = models.DateTimeField(auto_now=True, auto_now_add=True, help_text='Fecha de Registro', verbose_name=u'Fecha')

	def __unicode__(self):
		return self.CorreoDestino
