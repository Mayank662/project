from django import forms
from . models import survivorModel

class survivorForm(forms.ModelForm):

    class Meta:
        model = survivorModel
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
        super(survivorForm,self).__init__(*args, **kwargs)
        self.fields['name'].required = True