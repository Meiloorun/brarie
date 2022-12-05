from django import forms
from .models import Series, Season, Episode
from peopleapp.models import Person

class SeriesForm(forms.ModelForm):
    class Meta:

        model = Series

        fields = ['title', 'description', 'originalLanguage', 'status', 'genres']

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'formfield',
                'placeholder': 'Series Description',
                'rows': 25,
                'cols': 60,
            })
        }

class SeasonForm(forms.ModelForm):
    class Meta:

        model = Season

        fields = ['seasonNumber', 'title', 'description', 'year', 'status']

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'formfield',
                'placeholder': 'Season Description',
                'rows': 25,
                'cols': 60,
            })
        }

class EpisodeForm(forms.ModelForm):
    class Meta:

        model = Episode

        fields = ['episodeNumber', 'title', 'description', 'date', 'director', 'writer']

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'formfield',
                'placeholder': 'Episode Description',
                'rows': 25,
                'cols': 60,
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'formfield',
                'placeholder': 'yyyy-mm-dd HH-MM-SS',
                'format': '%d/%m/%Y %H/%M',
            }) 
        }