from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe

# Create your views here.
class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'

class RecipesDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'