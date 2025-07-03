from django.urls import path
from . import views

app_name = 'presence'

urlpatterns = [
    path('remplir/', views.remplir_semaine, name='remplir_semaine'),
    path('tableau/', views.voir_semaine, name='voir_semaine'),
]
