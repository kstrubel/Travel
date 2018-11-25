from django.urls import path

from . import views

urlpatterns = [
    path('<str:country_code>/', views.country, name='country'),
    path('', views.index, name='index'),
]