from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


        widgets = {
            'moviename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter language'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter about',}),
            'movieimg': forms.FileInput(attrs={'class': 'form-control'}),
        }


