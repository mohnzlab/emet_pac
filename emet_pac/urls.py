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
    url(r'^main/', 'emet.views.main', name="main"),
    url(r'^Alcaldes/', 'emet.views.mainAlcaldes', name="mainAlcaldes"),
    url(r'^Presidentes/', 'emet.views.mainPresidentes', name="mainPresidentes"),
    url(r'^logout_/', 'emet.views.salir', name="salir"),
)
