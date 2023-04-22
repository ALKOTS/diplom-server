# Generated by Django 4.1.7 on 2023-04-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0002_alter_activities_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='name',
        ),
        migrations.AddField(
            model_name='schedule',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedule',
            name='place',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='timeFinish',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='timeStart',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]