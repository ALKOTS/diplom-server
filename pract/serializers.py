from rest_framework import serializers
from pract.models import Workouts, Exercises


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = "__all__"


class WorkoutSeializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workouts
        fields = "__all__"
