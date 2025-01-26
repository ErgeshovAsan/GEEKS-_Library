from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Введите email')
    phon_number = forms.CharField(required=True, label='Введите номер телефона')
    expe = forms.IntegerField(required=True, label='Введите опыт')
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Укажите пол')
    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'expe',
            'gender',
            'phon_number',
        )

    def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.phon_number = self.cleaned_data['phon_number']
            user.expe = self.cleaned_data['expe']
            user.gender = self.cleaned_data['gender']

            if commit:
                user.save()
            return user