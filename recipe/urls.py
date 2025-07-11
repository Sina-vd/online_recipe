from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/edit/', views.update_recipe, name='update_recipe'),
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
]