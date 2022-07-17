# Generated by Django 4.0.4 on 2022-07-11 07:16

import custom_user.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('custom_user.user',),
            managers=[
                ('objects', custom_user.models.MyUserManager()),
            ],
        ),
    ]
