# Generated by Django 4.1.7 on 2023-04-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0008_remove_schedule_is_free_schedule_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
