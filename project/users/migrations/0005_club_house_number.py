# Generated by Django 4.0.2 on 2022-05-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_club_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='house_number',
            field=models.CharField(default=0, max_length=3000),
            preserve_default=False,
        ),
    ]
