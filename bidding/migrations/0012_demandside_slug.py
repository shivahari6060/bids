# Generated by Django 3.1.7 on 2021-03-22 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0011_supplyside_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandside',
            name='slug',
            field=models.CharField(default='maize', max_length=250),
        ),
    ]
