from django import forms
from .models import RecipeModel, IngredientModel

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = ['title', 'description']
        labels = {
            'title': 'Название',
            'description': 'Описание',
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientModel
        fields = ['name', 'quantity', 'unit']
        labels = {
            'name': 'Название',
            'quantity': 'Количество',
            'unit': 'Единица измерения',
        }