# Generated by Django 5.1.2 on 2024-10-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_customuser_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, max_length=120, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, max_length=120, null=True, upload_to='media/'),
        ),
    ]