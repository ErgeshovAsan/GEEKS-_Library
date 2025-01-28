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
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe_id'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)

class RecipeCreateView(generic.CreateView):
    form_class = forms.RecipeForm
    template_name = 'recipes/recipe_create.html'
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(RecipeCreateView, self).form_valid(form=form)

class IngredientCreateView(generic.CreateView):
    model = models.IngredientModel
    form_class = forms.IngredientForm
    template_name = 'recipes/ingredient_create.html'
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(IngredientCreateView, self).form_valid(form=form)

class RecipeDeleteView(generic.DeleteView):
    template_name = 'recipes/recipe_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)
