# Generated by Django 3.1.7 on 2021-03-22 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0006_auto_20210322_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplyside',
            name='country',
            field=models.ForeignKey(default='Nepal', null=True, on_delete=django.db.models.deletion.SET_NULL, to='bidding.country'),
        ),
    ]