from rest_framework import serializers
from pract.models import Workouts, Exercises, Activities, News


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
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
