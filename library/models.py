from django.db import models

class Books(models.Model):
    GENRE_CHOICES = (
        ('Фантастика', 'Фантастика'),
        ('Ужасы', 'Ужасы'),
        ('Боевик', 'Боевик'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.PositiveIntegerField(verbose_name='Укажите цену', default=500)
    created_at = models.DateTimeField(auto_now_add=True)
    genre_choices = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name='Выберите жанр', null=True)
    email = models.EmailField(verbose_name='Напишите почту')
    director = models.CharField(max_length=100, verbose_name='Укажите автора', default='Владимиров Иван')
    trailer = models.URLField(verbose_name='Укажите сылку с YOUTUBE')

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'список книг' \

    def __str__(self):
        return f'{self.title} - {self.price} сом'


