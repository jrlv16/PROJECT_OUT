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

def BonzaiDetail(request, bonzai_id):
    bonzai = get_object_or_404(Bonzai, pk=bonzai_id)
    return render(request, 'bonzai/detail_bonzai.html', {'object':bonzai})

class BonzaiListView(ListView):
    template_name = 'bonzai/bonzai.html'
            
    def get_queryset(self):
        type_arbre = self.kwargs.get('typarbre')
        if type_arbre:
            return Bonzai.objects.filter(type_arbre=type_arbre) 
        else:
            return Bonzai.objects.all() 
            