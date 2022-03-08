from django.db import models

gender_choice = (
    ('1','Male'),
    ('2','Female'),
    ('3','Unsure')
)
infected_choice = (
    (1,'Yes'),
    (0,'No')
)

class survivor_model(models.Model):
    name = models.CharField(max_length = 10)
    age = models.IntegerField()
    gender = models.CharField(choices = gender_choice, max_length = 4)
    latitude = models.FloatField()
    longitude = models.FloatField()
    infected = models.BooleanField(choices = infected_choice)

    
    