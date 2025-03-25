from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    search_fields = ('name', )


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInLine]

    search_fields = ('name', )

    ('Details', {
        'ingredients': [
            ('name', 'quantity'), 'image'
        ]
    })

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)