# Generated by Django 5.0 on 2023-12-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='image_app',
            field=models.ImageField(upload_to='images/', verbose_name='Фотография'),
        ),
    ]