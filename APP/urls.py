from django.urls import path
from . import views
from .views import BonzaiListView

urlpatterns = [
    path('', views.BonzaiListView.as_view(), name="accueil"),
    path('bonzai/<int:pk>', views.BonzaiDetailView.as_view(), name = 'detail_bonzai'),
    path('bonzai_cat/<str:typarbre>', views.BonzaiListView.as_view(), name= 'bonzai_par_type')
    ]