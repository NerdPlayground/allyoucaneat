# Generated by Django 4.0.4 on 2022-07-11 07:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='products.product')),
            ],
        ),
    ]
