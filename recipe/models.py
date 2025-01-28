from django.db import models

class RecipeModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='название рецепта')
    description = models.TextField(verbose_name='описание рецепта')

    def __str__(self):
        return self.title


class IngredientModel(models.Model):
    UNIT = (
        ('граммы', 'граммы'),
        ('килограммы', 'килограммы'),
        ('миллилитры', 'миллилитры'),
        ('литры', 'литры'),
        ('штуки', 'штуки'),
    )
    name = models.CharField(max_length=300, verbose_name='название ингредиента')
    quantity = models.PositiveIntegerField(verbose_name='количество')
    unit = models.CharField(max_length=10, choices=UNIT, verbose_name='единица измерения')
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
