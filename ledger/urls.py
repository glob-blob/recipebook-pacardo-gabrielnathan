from django.urls import path
from .views import RecipesListView, RecipesDetailView, RecipeCreateView, RecipeImageUpdateView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name="recipes-list"),
    path('recipe/<int:pk>', RecipesDetailView.as_view(), name='recipe'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/add_image', RecipeImageUpdateView.as_view(), name='recipe-update-img')
]

app_name = "ledger"