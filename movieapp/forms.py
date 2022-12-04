from django import forms
from .models import Movie
from peopleapp.models import Person

class MovieForm(forms.ModelForm):
    class Meta:
        years = []

        for i in range(1, 2040):
            years.append(i)
        
        model = Movie

        fields = ['title', 'releaseDate', 'description', 'status', 'genres', 'ageRating', 'director', 'writer', 'originalLanguage']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'Movie Title', 
            }),
            'releaseDate' : forms.SelectDateWidget(attrs={
                'class': 'formfield',
                'years': years,
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
            'ageRating': forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'Movie Age Rating',
            }),
            'originalLanguage': forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'Movie Original Language',
            })
        }
