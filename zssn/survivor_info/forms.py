from django import forms
from . models import survivor_model

class survivor(forms.ModelForm):

    class Meta:
        model = survivor_model
        fields = ('name','age','gender','latitude','longitude','infected')

        labels = {
        'name' : 'Name',
        'age' : 'Age',
        'gender' : 'Gender',
        'latitude' : 'Latitude',
        'longitude':'Longitude',
        'infected':'Isinfected'
    }
    def __init__(self, *args, **kwargs):
        super(survivor,self).__init__(*args, **kwargs)
        self.fields['name'].required = True