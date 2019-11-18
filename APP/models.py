from django.db import models


# Create your models here.


class TypeFeuille(models.Model):
    name = models.CharField(max_length=15, default="Indefini")
        
    def __str__(self):
        return self.name

class Bonzai(models.Model):
    nom = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    taille = models.DecimalField(max_digits=3, decimal_places=2)
    pays_origine = models.CharField(max_length=15, blank=False, null=False)
     
    
    FEUILLU_CADUQUE = 'FEUIL-CADU'
    FEUILLU_PERSISTANT = 'FEUIL-PERS'
    CONIFERE_PERSISTANT = 'CONIF-PERS'
    TYPE_ARBRE_CHOICES =[
        (FEUILLU_CADUQUE, 'FEUILLU CADUQUE'),
        (FEUILLU_PERSISTANT, 'FEUILLU PERSISTANT'),
        (CONIFERE_PERSISTANT, 'CONIFERE PERSISTANT')
        ]
        
    type_arbre = models.CharField(max_length=10,
        choices = TYPE_ARBRE_CHOICES,
        default= FEUILLU_CADUQUE,
        verbose_name ="Type d'arbre"
    ) 

    type_feuille = models.ForeignKey(TypeFeuille, on_delete=models.CASCADE)
    provenance = models.CharField(max_length=20)
    img_arbre = models.ImageField(null = True, blank = True, upload_to='logo')

    def __str__(self): 
        return '{} {}'.format(self.nom, self.type_arbre)
    
    @classmethod
    def BonzaiSearchList(cls):
        l = cls.TYPE_ARBRE_CHOICES
        ltype =[]
        typedict={}    
        for t in l:
            typedict[t[0]] = t[1]
            ltype.append(typedict)
            typedict={}
        
        extra = {'ltreetype': ltype}
        return extra



