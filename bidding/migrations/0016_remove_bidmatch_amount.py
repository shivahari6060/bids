# Generated by Django 3.1.7 on 2021-03-23 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0015_auto_20210323_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidmatch',
            name='amount',
        ),
    ]