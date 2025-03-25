from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=20)
    ingredient = models.ForeignKey(Ingredient, 
                                    on_delete=models.SET_NULL, 
                                    null=True, 
                                    related_name='recipe')
    recipe = models.ForeignKey(Recipe, 
                               on_delete=models.SET_NULL,
                               null=True, 
                               related_name='ingredients')
    

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255)
    recipe =  models.ForeignKey(Recipe, 
                                    on_delete=models.CASCADE, 
                                    null=False, 
                                    related_name='image')