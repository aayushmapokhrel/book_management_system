from django import forms
from book.models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'