# Generated by Django 4.0.2 on 2022-03-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='survivor_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Unsure')], max_length=4)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('infected', models.BooleanField(choices=[('1', 'Yes'), ('2', 'No')])),
            ],
        ),
    ]
