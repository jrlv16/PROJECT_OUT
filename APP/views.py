from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Bonzai
from .forms import BonzaiForm


# Create your views here.
# une méthode créée comme une fonction

# def index(request):
#     context = {'bonzai_list' : Bonzai.objects.all(),}               
#     return render(request, 'bonzai/bonzai.html', context)

extra = Bonzai.BonzaiSearchList()

class BonzaiDetailView(DetailView):
    model = Bonzai
    extra_context = extra
    template_name ='bonzai/detail_bonzai.html'

def BonzaiDetail(request, bonzai_id):
    
    bonzai = get_object_or_404(Bonzai, pk=bonzai_id)
    context = {'bonzai_list': Bonzai.objects.all(), **extra}
    return render(request, 'bonzai/detail_bonzai.html', context)

class BonzaiListView(ListView):
    template_name = 'bonzai/bonzai.html'
    extra_context = extra    
            
    def get_queryset(self):
        type_arbre = self.kwargs.get('typarbre')
        if type_arbre:
            return Bonzai.objects.filter(type_arbre=type_arbre) 
        else:
            return Bonzai.objects.all()

def BonzaiList(request):
    context = {'bonzai_list': Bonzai.objects.all(), **extra}
    return render(request, 'bonzai/bonzai.html', context)


def BonzaiCreate(request):
    template = 'bonzai/bonzai_form.html'
    form = BonzaiForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accueil')
    context = {"form": form, **extra}
    return render(request, template, context)

def bonzai_update(request, pk):
    template = 'bonzai/bonzai_form.html'
    bonzai = get_object_or_404(Bonzai, pk=pk)
    form = BonzaiForm(request.POST or None, instance=bonzai)
    if form.is_valid():
        form.save()
        return redirect('detail_bonzai', pk)
    context = {"form": form, **extra}
    return render(request, template, context)

def bonzai_delete(request, pk):
    template = 'bonzai/bonzai_delete.html'
    bonzai = get_object_or_404(Bonzai, pk=pk)
    if request.method == 'POST':
        bonzai.delete()
        return redirect('accueil')
    context = {"bonzai": bonzai, **extra}
    return render(request, template, context)