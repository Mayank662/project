from django import forms

gender_choice = (
    ('1','Male'),
    ('2','Female'),
    ('3','Unsure')
)

infected_choice = (
    ('1','Yes'),
    ('2','No')
)

class survivor(forms.Form):
    name = forms.CharField(max_length = 10)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices = gender_choice)
    latitude = forms.IntegerField()
    longitude = forms.CharField()
    infected = forms.ChoiceField(choices = infected_choice)

    labels = {
        'name' : 'Name',
        'age' : 'Age',
        'gender' : 'Gender',
        'latitude' : 'Latitude',
        'longitude':'Longitude',
        'infected':'Infected'
    }