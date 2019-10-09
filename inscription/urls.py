from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path ('enregistrement/', views.register, name='register'),
    path ('connexion/', views.loginUser, name='login'),
    path ('deconnexion/', views.logoutUser, name='logout'),
    path ('modif_pass/', views.change_password, name='changepass')
]
