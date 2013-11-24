from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'emet.views.home', name='home'),
    # url(r'^emet_pac/', include('emet_pac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'emet.views.ingresar', name="ingresar"),
    url(r'^main/$', 'emet.views.main', name="main"),
    url(r'^main/Alcaldes/$', 'emet.views.mainAlcaldes', name="mainAlcaldes"),
    url(r'^main/Presidentes/$', 'emet.views.mainPresidentes', name="mainPresidentes"),
    url(r'^main/Diputados/$', 'emet.views.mainDiputados', name="mainDiputados"),
    url(r'^main/Diputados/Filtrar/$', 'emet.views.FiltrarDiputados', name="FiltrarDiputados"),
    url(r'^main/Reportes/Alcaldes/$', 'emet.views.ReportesAlcades', name="ReportesAlcades"),
    url(r'^main/Reportes/Presidentes/$', 'emet.views.ReportesPresidentes', name="ReportesPresidentes"),
    url(r'^main/Reportes/Diputados/$', 'emet.views.ReportesDiputados', name="ReportesDiputados"),
    url(r'^main/Presidentes/ActaPresidente/$', 'emet.views.ActaPresidenteAdd', name="ActaPresidenteAdd"),
    url(r'^main/Diputados/ActaDiputado/$', 'emet.views.ActaDiputadoAdd', name="ActaDiputadoAdd"),
    url(r'^main/Alcaldes/ActaAlcalde/$', 'emet.views.ActaAlcaldeAdd', name="ActaAlcaldeAdd"),
    url(r'^logout_/', 'emet.views.salir', name="salir"),
    url(r'^DatosDiputados/$', 'emet.views.DatosDiputados', name='DatosDiputados'),
    url(r'^DatosCuadroAlcaldes/$', 'emet.views.MostrarResultadosAlcaldesGrafica', name='MostrarResultadosAlcaldesGrafica'),
    url(r'^DatosCuadroDiputados/$', 'emet.views.Mostrar9DiputadosGanando', name='Mostrar9DiputadosGanando'),
    url(r'^DatosAlcaldes/$', 'emet.views.DatosAlcaldes', name='DatosAlcaldes'),
    url(r'^DatosPresidentes/$', 'emet.views.DatosPresidentes', name='DatosPresidentes'),
    url(r'^Dashboard/$', 'emet.views.Dashboard', name='Dashboard'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}, ),
)
