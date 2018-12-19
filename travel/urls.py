from django.urls import path

from . import views

urlpatterns = [
    path('country/<str:country_code>/', views.country, name='country'),
    path('', views.index, name='index'),
]