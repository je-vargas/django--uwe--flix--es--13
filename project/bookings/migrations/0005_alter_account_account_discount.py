# Generated by Django 4.0.2 on 2022-05-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_logintransaction_club_account_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_discount',
            field=models.FloatField(default=0, null=True),
        ),
    ]
