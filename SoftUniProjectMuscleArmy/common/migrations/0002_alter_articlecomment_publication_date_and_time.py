# Generated by Django 5.0.3 on 2024-04-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='publication_date_and_time',
            field=models.DateTimeField(blank=True, default=True),
        ),
    ]
