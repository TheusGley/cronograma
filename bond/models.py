from django.db import models

class Evento (models.Model):
    cidade =  models.CharField(max_length=100)
    servidor =  models.CharField(max_length=100)
    data = models.DateField( auto_now=False, auto_now_add=False)
    assunto = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.cidade
        
        