# Generated by Django 4.0.2 on 2022-03-08 17:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_title', models.CharField(max_length=50)),
                ('account_discount', models.BigIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_cost', models.IntegerField()),
                ('number_of_tickets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.BigIntegerField()),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
                ('club_guid', models.UUIDField(default=uuid.uuid4)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landline', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('age_rating', models.BigIntegerField()),
                ('duration', models.CharField(max_length=10)),
                ('film_description', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('createdOn', models.DateTimeField()),
                ('last_logged_in', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_number', models.IntegerField()),
                ('screen_seats_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateTimeField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_app.account')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_app.booking')),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_app.club')),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.film')),
            ],
        ),
        migrations.CreateModel(
            name='ScreenShowings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.screen')),
                ('showing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.showing')),
            ],
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('unique_number', models.UUIDField(default=uuid.uuid4)),
                ('unique_password', models.CharField(max_length=50)),
                ('login_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.loginaccount')),
            ],
        ),
        migrations.CreateModel(
            name='ClubRepresentative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_app.club')),
                ('representative_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.representative')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='contact_details_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.contactdetails'),
        ),
        migrations.CreateModel(
            name='BookedTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.booking')),
                ('screen_showing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.showing')),
                ('ticket_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.tickettype')),
            ],
        ),
        migrations.CreateModel(
            name='AccountRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.loginaccount')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_app.roles')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='card_details_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_app.carddetails'),
        ),
    ]
