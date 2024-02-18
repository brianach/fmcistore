from django.db import models

# Create your models here.

class PartnerImages(models.Model):

    p_name = models.CharField(max_length=254)
    p_image = models.ImageField(null=True, blank=True)
    p_link = models.CharField(max_length=254)

    def __str__(self):
        return self.p_name