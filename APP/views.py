from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Bonzai

# Create your views here.
# une méthode créée comme une fonction

def index(request):
    context = {'bonzai_list' : Bonzai.objects.all(),}               
    return render(request, 'bonzai/bonzai.html', context)

class BonzaiDetailView(DetailView):
    model = Bonzai
    template_name ='bonzai/detail_bonzai.html'

class BonzaiListView(ListView):
    template_name = 'bonzai/bonzai.html'
    def get_queryset(self):
        return Bonzai.objects.filter(type_arbre= self.kwargs.get('typarbre')) 
