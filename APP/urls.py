from django.urls import path
from . import views
from .views import BonzaiListView

urlpatterns = [
    path('', views.BonzaiList, name="accueil"),
    path('bonzai/<int:pk>', views.BonzaiDetailView.as_view(), name = 'detail_bonzai'),
    path('bonzai_cat/<str:typarbre>', views.BonzaiListView.as_view(), name= 'bonzai_par_type'),
    path('bonzai/create', views.BonzaiCreate, name='bonzai_create'),
    path('bonzai/update/<int:pk>', views.bonzai_update, name='bonzai_update'),
    path('bonzai/delete/<int:pk>', views.bonzai_delete, name='bonzai_delete'),
    ]