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
    url(r'^main/Reportes/$', 'emet.views.mainPresidentes', name="mainPresidentes"),
    url(r'^main/Presidentes/ActaPresidente/$', 'emet.views.ActaPresidenteAdd', name="ActaPresidenteAdd"),
    url(r'^main/Diputados/ActaDiputado/$', 'emet.views.ActaDiputadoAdd', name="ActaDiputadoAdd"),
    url(r'^main/Alcaldes/ActaAlcalde/$', 'emet.views.ActaAlcaldeAdd', name="ActaAlcaldeAdd"),
    url(r'^logout_/', 'emet.views.salir', name="salir"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT},
        ),
)
