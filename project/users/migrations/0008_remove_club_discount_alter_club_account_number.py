# Generated by Django 4.0.2 on 2022-05-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_club_account_number_alter_club_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='discount',
        ),
        migrations.AlterField(
            model_name='club',
            name='account_number',
            field=models.UUIDField(default='05927290-2534-457f-9f8f-4bca2e9e01bc'),
            preserve_default=False,
        ),
    ]