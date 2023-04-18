from rest_framework import serializers
from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from pract.models import (
    Workouts,
    Exercises,
    Schedule,
    Activities,
    News,
    Clients,
    Trainer,
    Appointments,
)
from django.core.validators import validate_email


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(many=False)

    class Meta:
        model = Exercises
        fields = "__all__"


class WorkoutSeializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workouts
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(many=False)
    leader = TrainerSerializer(many=False)

    class Meta:
        model = Schedule
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ["username", "last_name", "email", "login"]


class AppointmentsSerializer(serializers.ModelSerializer):
    schedule_position = ScheduleSerializer(many=False)

    class Meta:
        model = Appointments
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ("login", "username", "last_name", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        # client = Clients(email=self.validated_data["email"])
        password = self.validated_data["password"]  # .pop("password")
        client = Clients(**self.validated_data)
        client.set_password(password)
        client.save()
        return client
