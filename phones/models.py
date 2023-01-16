from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=200, null = False)
    image = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    release_date = models.DateField(auto_now_add=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, blank=True,unique=True)
    
