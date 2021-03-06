from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

# Create your models here.


class Categori(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
 
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
 
    def __str__(self):
        return self.name


class Products(models.Model):

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True) #Heading Text
    description = models.TextField(blank=True)
    category = models.ForeignKey(Categori, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True) #Quantity


    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
 

    def __str__(self):
        return self.name

