

from django.db import models


# Create your models here.
class Employe(models.Model):
   name = models.CharField(max_length=50)
   father = models.IntegerField(null=True, blank=True)
   mother = models.IntegerField(null=True, blank=True)
   email = models.EmailField(blank=True, null=True)
   code = models.IntegerField(blank=True, null=True)
   phone = models.IntegerField(blank=True, null=True)
   address = models.TextField(blank=True, null=True)

   def __str__(self):
      return self.name
