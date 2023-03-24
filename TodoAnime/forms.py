from django import forms
from TodoAnime.models import Otaku

class OtakuForm(forms.ModelForm):
    class Meta:
        model = 'Otaku'
        fields = '__all__'