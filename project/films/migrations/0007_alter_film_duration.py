# Generated by Django 4.0.2 on 2022-05-03 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_rename_card_details_id_account_card_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
