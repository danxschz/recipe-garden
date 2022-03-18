from django.db import models
from django.core.validators import MinLengthValidator

class Source(models.Model):
    web = models.CharField(
            max_length=128,
            validators=[MinLengthValidator(3, "Web name must be greater than 2 characters")]
    )

    def __str__(self):
        return self.web

class Author(models.Model):
    name = models.CharField(
            max_length=128,
            validators=[MinLengthValidator(3, "Author name must be greater than 2 characters")]
    )
    source = models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(
            max_length=128,
            validators=[MinLengthValidator(3, "Ingredient name must be greater than 2 characters")]
    )

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(3, "Category name must be greater than 2 characters")],
    )

    class Meta:
        verbose_name_plural = "Categories" # Change name in admin interface

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(3, "Recipe name must be greater than 2 characters")]
    )
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    prep_time = models.IntegerField(null=True, blank=True) 
    servings = models.IntegerField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', related_name='recipe_ingredients')
    directions = models.TextField()
    nutrition_facts = models.TextField(blank=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #rating 
    #comments
    #pictures
    #owner/made_by
    #saves/favorites

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        recipe_ingredient_str = f'{self.ingredient.name} used in {self.recipe.name}'
        return recipe_ingredient_str



