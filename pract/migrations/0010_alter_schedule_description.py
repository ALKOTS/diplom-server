# Generated by Django 4.1.7 on 2023-04-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0009_schedule_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
