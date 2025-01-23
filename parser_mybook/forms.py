from django import forms
from . import models, parser_mybook

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('mybook', 'mybook'),
        ('l', 'l')
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type'
        ]

    def parser_data(self):
        if self.data['media_type'] == 'mybook':
            file_mybook = parser_mybook.parsing()
            for i in file_mybook:
                models.MyBookParser.objects.create(**i)