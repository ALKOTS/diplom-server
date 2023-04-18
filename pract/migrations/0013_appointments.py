# Generated by Django 4.1.7 on 2023-04-18 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0012_rename_finishtime_schedule_endtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('schedule_position', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pract.schedule')),
            ],
            options={
                'db_table': 'appointments',
                'managed': True,
            },
        ),
    ]
