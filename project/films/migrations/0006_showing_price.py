# Generated by Django 4.0.2 on 2022-05-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_showing_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='showing',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]