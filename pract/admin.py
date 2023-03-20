from django.contrib import admin
from pract.models import (
    Activities,
    Clients,
    Trainer,
    Schedule,
    News,
    Exercises,
    Workouts,
)

admin.site.register(Activities),
admin.site.register(Clients),
admin.site.register(Trainer),
admin.site.register(Schedule),
admin.site.register(News),
admin.site.register(Exercises),
admin.site.register(Workouts)
