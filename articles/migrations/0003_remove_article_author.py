# Generated by Django 4.2.5 on 2023-09-17 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_article_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="author",
        ),
    ]
