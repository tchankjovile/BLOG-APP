# Generated by Django 5.1.2 on 2024-10-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_article_image_alter_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sexe',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
