# Generated by Django 4.1.7 on 2023-04-16 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0004_schedule_people_enlisted_alter_schedule_people_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='workout_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='pract.workouts'),
        ),
    ]