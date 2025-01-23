from django.db import models

class MyBookParser(models.Model):
    title = models.CharField(max_length=500)
    href = models.URLField()

    def __str__(self):
        return self.title
