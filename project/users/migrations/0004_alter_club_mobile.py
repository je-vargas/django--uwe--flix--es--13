# Generated by Django 4.0.2 on 2022-05-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_club_landline_alter_club_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='mobile',
            field=models.CharField(max_length=13),
        ),
    ]
