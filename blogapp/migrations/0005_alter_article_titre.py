# Generated by Django 5.1.2 on 2024-10-20 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_alter_customuser_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
