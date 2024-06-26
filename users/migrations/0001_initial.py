# Generated by Django 5.0.4 on 2024-06-20 19:41

import django.db.models.deletion
import users.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=124)),
                ('address_2', models.CharField(blank=True, max_length=124)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(default='NY', max_length=64)),
                ('zip_code', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to=users.utils.user_directory_path)),
                ('bio', models.CharField(blank=True, max_length=140)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
