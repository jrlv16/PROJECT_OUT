from django.shortcuts import render, get_object_or_404
from .models import Bonzai

# Create your views here.
# une méthode créée comme une fonction

def index(request):
    # bonzai = '/' + bonzai
    # pg = get_object_or_404(Bonzai)
    
    context = {'bonzai_list' : Bonzai.objects.all(),
                }
    
    # assert False # permet de tester l'affichage de la page
    
    return render(request, 'bonzai/bonzai.html', context)

