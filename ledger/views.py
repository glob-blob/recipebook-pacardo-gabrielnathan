from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'


class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'