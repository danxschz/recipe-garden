from django.contrib import admin
from .models import Category, Recipe, Unit, Ingredient, Source, Author, RecipeIngredient

# Register your models here.
admin.site.register(Source)
admin.site.register(Author)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)