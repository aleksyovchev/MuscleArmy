# Generated by Django 5.0.3 on 2024-04-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_articlecomment_publication_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='publication_date_and_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
