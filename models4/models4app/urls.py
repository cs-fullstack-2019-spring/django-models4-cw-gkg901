from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('citizens', views.citizens, name='citizens'),
    path('chgstate', views.chgstate, name='chgstate'),
]
