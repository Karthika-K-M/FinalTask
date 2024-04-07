from django import forms
from . models import Movies

class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields=['title','desc','releasedate','img','actors','category','trailer']