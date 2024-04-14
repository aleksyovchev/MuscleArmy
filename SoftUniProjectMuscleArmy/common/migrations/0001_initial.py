# Generated by Django 5.0.3 on 2024-03-28 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0003_alter_article_article_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='common.articlecomment')),
            ],
        ),
    ]
