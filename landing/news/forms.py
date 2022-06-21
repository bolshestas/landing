from django import forms
from .models import News


class Newsform(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        # ^ описание всех полей в форме
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }