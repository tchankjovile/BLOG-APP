# Generated by Django 5.1.2 on 2024-10-20 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_alter_article_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
