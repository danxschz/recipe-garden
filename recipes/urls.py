from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredient_list'),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipes/ingredient/<slug:slug>/', views.RecipesByIngredient.as_view(), name='recipes_by_ingredient'),
    path('recipes/category/<slug:slug>/', views.RecipesByCategory.as_view(), name='recipes_by_category'),
]
