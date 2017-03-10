from django import forms

from .models import  Place


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')


class DateInput(forms.DateInput):
    input_type = 'date'


class PlaceVisitedForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('place_review', 'date', 'visited')
        widgets = {
            'date': DateInput(),
        }

