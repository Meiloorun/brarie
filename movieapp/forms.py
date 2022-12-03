from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie

        fields = ['title', 'releaseDate', 'description', 'status', 'genres', 'ageRating', 'director', 'writer', 'originalLanguage']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'Movie Title', 
            }),
            'releaseDate' : forms.DateInput(attrs={
                'class': 'formfield',
            }),
            'description': forms.Textarea(attrs={
                'class': 'formfield',
                'placeholder': 'Movie Description',
                'rows': 25,
                'cols': 60,
            }),
            'status': forms.NumberInput(attrs={
                'class': 'formfield',
                'placeholder': 0,
            }),
            'genres': forms.Textarea(attrs={
                'class': 'formfield',
                'placeholder': 'Movie Genres',
                'rows': 10,
                'cols': 35,
            }),
            'ageRating': forms.Textarea(attrs={
                'class': 'formfield',
                'placeholder': 'Movie Age Rating',
            }),
        }
