# Generated by Django 4.1.7 on 2023-03-20 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0002_alter_exercises_workout_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='workout_id',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='pract.workouts'),
        ),
    ]