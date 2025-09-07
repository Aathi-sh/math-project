from django import forms
from .models import MathPuzzle

class MathPuzzleForm(forms.ModelForm):
    
    class Meta:
        model = MathPuzzle
        fields = ['name','title','author','row','cols','difficulty','grid','solution','created_by','updated_by']
