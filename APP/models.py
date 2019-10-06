from django.db import models


# Create your models here.



class Bonzai(models.Model):
    nom = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    taille = models.DecimalField(max_digits=3, decimal_places=2)
    pays_origine = models.CharField(max_length=15, blank=False, null=False)
     
    ENTR =[]
    FEUILLU_CADUQUE = 'FEUIL-CADU'
    FEUILLU_PERSISTANT = 'FEUIL-PERS'
    CONIFERE_PERSISTANT = 'CONIF-PERS'
    TYPE_ARBRE_CHOICES =(
        (FEUILLU_CADUQUE, 'FEUILLU_CADUQUE'),
        (FEUILLU_PERSISTANT, 'FEUILLU_PERSISTANT'),
        (CONIFERE_PERSISTANT, 'CONIFERE_PERSISTANT')
        )
    type_arbre = models.CharField(max_length=10,
        choices = TYPE_ARBRE_CHOICES,
        default= FEUILLU_CADUQUE,
        verbose_name ="Type d'arbre"
    ) 
    provenance = models.CharField(max_length=20)
    img_arbre = models.ImageField(null = True, blank = True, upload_to='logo')

    def __str__(self): 
        return '{} {}'.format(self.nom, self.type_arbre)

           