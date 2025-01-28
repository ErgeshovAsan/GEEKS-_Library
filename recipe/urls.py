from django.urls import path
from . import views
urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe_detail/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe_create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('ingredient_create/<int:recipe_id>/add_ingredient/', views.IngredientCreateView.as_view(), name='ingredient_create'),
    path('recipe_delete/<int:id>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    ]