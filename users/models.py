from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phon_number = models.CharField(max_length=14)
    expe = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    club = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.expe < 1:
            self.club = "У вас мало опыта, приходитье поднабрав опыта."
        elif 1 <= self.expe <= 3:
            self.club = 'Зарплата 1000$'
        elif 3 < self.expe <= 7:
            self.club = 'Зарплата 2000$'
        elif 7 < self.expe <= 10:
            self.club = 'Зарплата 5000$'
        else:
            self.club = "Для вас нет работы"

        super().save(*args, **kwargs)
