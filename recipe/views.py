from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

class RecipeListView(generic.ListView):
    model = models.RecipeModel
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")

class RecipeDetailView(generic.DetailView):
    model = models.RecipeModel
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredientmodel_set.all()
        return context

class RecipeCreateView(generic.CreateView):
    form_class = forms.RecipeForm
    template_name = 'recipes/recipe_create.html'
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class IngredientCreateView(generic.CreateView):
    model = models.IngredientModel
    form_class = forms.IngredientForm
    template_name = 'recipes/ingredient_create.html'

    def form_valid(self, form):
        recipe = get_object_or_404(models.RecipeModel, id=self.kwargs['recipe_id'])
        ingredient = form.save(commit=False)
        ingredient.recipe = recipe
        ingredient.save()
        return redirect('recipe_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(models.RecipeModel, id=self.kwargs['recipe_id'])
        return context

class RecipeDeleteView(generic.DeleteView):
    model = models.RecipeModel
    template_name = 'recipes/recipe_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)
