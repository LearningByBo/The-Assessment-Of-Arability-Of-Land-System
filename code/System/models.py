from django.db import models
from sklearn import tree

# Create your models here.
class Factor(models.Model):
    organic_matter = models.IntegerField()
    total_nitrogen = models.IntegerField()
    available_P = models.IntegerField()
    available_K = models.IntegerField()

    def __unicode__ (self):
        return self.organic_matter + self.total_nitrogen + self.available_P + self.available_K

    def generate_Desicion(self):
        factors = self.objects.all()
        dataset = []
        for factor in factors:
            dataset += [factor.organic_matter,factor.total_nitrogen,factor.available_P,factor.available_K]
        