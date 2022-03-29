from django.urls import path

from . import views

urlpatterns = [
    path('cards/', views.index, name='index'),
    path('cards/<int:id>/', views.detail, name='detail'),
    path('', views.home, name='home'),
]