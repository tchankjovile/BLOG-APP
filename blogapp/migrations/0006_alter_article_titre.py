# Generated by Django 5.1.2 on 2024-10-20 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_article_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
