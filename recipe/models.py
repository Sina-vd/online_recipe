from django.db import models


class Recipe(models.Model):
    levels = [(1, "easy"), (2, "medium"), (3, "hard")]
    title = models.CharField(max_length=100)
    description = models.TextField()
    instruction = models.TextField()
    prep_time = models.DurationField()
    cooking_time = models.DurationField()
    difficulty_level = models.IntegerField(choices=levels, default=2)
    # Ingredient = models.ManyToManyField("ingredient",related_name="recipe_ingredient")
    def __str__(self):
        return str(self.title)

class Category(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ManyToManyField(Recipe,related_name="recipe")

    def __str__(self):
        return str(self.name)
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity =models.SmallIntegerField()
    recipe =models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='ingredients')
    def __str__(self):
        return f"{self.quantity} {self.name} for {self.recipe}"
    