from django.urls import path
from .views import RecipesListView, RecipesDetailView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name="recipes-list"),
    path('recipe/<int:pk>', RecipesDetailView.as_view(), name='recipe'),
]

app_name = "ledger"