from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Ingredient
from .forms import RecipeForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe.objects.prefetch_related("ingredients"), id=recipe_id)
    ingredients = recipe.ingredients.all()
    return render(request, 'recipe_details.html', {'recipe': recipe, 'ingredients': ingredients})

def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'update_recipe.html', {'form': form, 'recipe': recipe})

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 't.html', {'recipe': recipe})    