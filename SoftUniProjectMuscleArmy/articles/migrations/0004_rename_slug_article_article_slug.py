# Generated by Django 5.0.3 on 2024-04-01 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_article_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='slug',
            new_name='article_slug',
        ),
    ]
