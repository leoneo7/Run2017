from django import forms
from cms.models import Track


class TrackForm(forms.ModelForm):
    distance = forms.CharField(label='走行距離')
    date = forms.CharField(label='日付')

    class Meta:
        model = Track
        fields = ('distance', 'date',)