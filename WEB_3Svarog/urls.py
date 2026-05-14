from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("", views.index, name="index"),
    path("leistungen", views.leistungen, name="leistungen"),
    path("kontakt", views.kontakt, name="kontakt"),
    path("projekte", views.projekte, name="projekte"),
    path("datenschutz", views.datenschutz, name="datenschutz"),
    path("impressum", views.impressum, name="impressum"),
    path('i18n/', include('django.conf.urls.i18n')),
]
