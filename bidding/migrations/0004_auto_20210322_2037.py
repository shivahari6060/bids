# Generated by Django 3.1.7 on 2021-03-22 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_auto_20210322_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='country',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='district',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='municipality',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='province',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
