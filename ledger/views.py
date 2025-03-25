from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from .forms import RecipeImageForm
from .models import Recipe, RecipeImage

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'


class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'


class RecipeCreateView(CreateView):
    model = Recipe
    fields = '__all__'


class RecipeImageUpdateView(UpdateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_update_img.html'
    
    def get_object(self):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        recipe_image, create = RecipeImage.objects.get_or_create(recipe=recipe)
        return recipe_image
    
    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={ 'pk': self.object.recipe.pk })
