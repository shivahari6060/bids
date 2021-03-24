# Generated by Django 3.1.7 on 2021-03-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0014_auto_20210323_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidmatch',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='bidmatch',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bidmatch',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]