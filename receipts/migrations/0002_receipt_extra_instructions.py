# Generated by Django 4.0.4 on 2022-11-05 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='extra_instructions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
