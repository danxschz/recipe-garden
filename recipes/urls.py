from django.urls import path
from . import views
from django.conf import settings

app_name = 'recipes'
urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredient_list'),
    path('recipes/ingredient/<slug:slug>/', views.RecipesByIngredient.as_view(), name='recipes_by_ingredient'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('recipes/category/<slug:slug>/', views.RecipesByCategory.as_view(), name='recipes_by_category'),
]
