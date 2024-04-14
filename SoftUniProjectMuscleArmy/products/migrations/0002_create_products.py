# Generated by Django 5.0.3 on 2024-03-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('old_price', models.CharField(blank=True, max_length=10, null=True)),
                ('size', models.CharField(max_length=3)),
                ('product_photo', models.URLField()),
            ],
        ),
    ]