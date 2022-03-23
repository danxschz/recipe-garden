from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse, reverse_lazy
from django.views import View
from .models import Recipe, Ingredient, RecipeIngredient, Category

class RecipeList(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipe_list'

class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Ingredients
        ingredients = RecipeIngredient.objects.filter(recipe=self.object)
        context['ingredients'] = ingredients

        # Directions
        directions = self.object.directions.split('\n')
        context['directions'] = directions

        # Similar recipes
        similar_recipes = Recipe.objects.filter(category=self.object.category)
        similar_recipes = similar_recipes.exclude(name=self.object.name)[0:4]
        context['similar_recipes'] = similar_recipes

        return context

class IngredientList(ListView):
    model = Ingredient
    template_name = 'recipes/ingredient_list.html'
    queryset = Ingredient.objects.order_by('name')
    context_object_name = 'ingredient_list'

class RecipesByIngredient(View):
    template_name = 'recipes/recipes_by_ingredient.html'

    def get(self, request, slug):
        ingredient = Ingredient.objects.get(slug=slug)
        queryset = RecipeIngredient.objects.filter(ingredient=ingredient)
        context = {'recipe_list': queryset, 'ingredient': ingredient}
        return render(request, self.template_name, context)

class CategoryList(ListView):
    model = Category
    template_name = 'recipes/category_list.html'
    queryset = Category.objects.order_by('name')
    context_object_name = 'category_list'

class RecipesByCategory(View):
    template_name = 'recipes/recipes_by_category.html'

    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        queryset = Recipe.objects.filter(category=category)
        context = {'recipe_list': queryset, 'category': category}
        return render(request, self.template_name, context)


