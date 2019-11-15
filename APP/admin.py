from django.contrib import admin
from .models import Bonzai, TypeFeuille

# Register your models here.

class BonzaiAdmin(admin.ModelAdmin):
    model = Bonzai
    list_display = ['nom', 'type_arbre', 'pays_origine', 'age']
    list_filter = ['nom', 'type_arbre', 'age']
    search_fields = ['nom', 'type_arbre', 'age']
admin.site.register(Bonzai, BonzaiAdmin)

class TypeFeuilleAdmin(admin.ModelAdmin):
    model = TypeFeuille
admin.site.register(TypeFeuille, TypeFeuilleAdmin)    