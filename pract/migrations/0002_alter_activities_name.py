# Generated by Django 4.1.7 on 2023-04-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]