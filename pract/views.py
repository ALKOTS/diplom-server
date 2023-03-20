from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework import generics
from pract.serializers import WorkoutSeializer

from pract.models import (
    Clients,
    Activities,
    Schedule,
    Trainer,
    News,
    Workouts,
    Exercises,
)

# from models import get_clients

# Create your views here.
def return_client_info(request):
    clients = []
    # Clients.objects.raw("SELECT * FROM clients", translations=name_map)
    for c in Clients.objects.raw("SELECT * FROM clients"):
        clients.append(
            {"name": c.name, "last_name": c.last_name, "password": c.password}
        )

    return JsonResponse({"client": clients})


def return_activities_info(request):
    activities = []
    # Clients.objects.raw("SELECT * FROM activities", translations=name_map)
    for c in Activities.objects.raw("SELECT * FROM activities"):
        activities.append(
            {
                "name": c.name,
                "beginner_friendly": c.beginner_friendly,
                "crossfit": c.crossfit,
                "general_workout": c.general_workout,
                "cardio": c.cardio,
                "legs": c.legs,
                "chest": c.chest,
                "shoulders": c.shoulders,
                "biceps": c.biceps,
                "triceps": c.triceps,
                "is_group": c.is_group,
                "is_competition": c.is_competition,
            }
        )

    return JsonResponse({"activity": activities})


def return_trainer_info(request):
    trainers = []
    for c in Trainer.objects.all():
        trainers.append(
            {
                "id": c.id,
                "name": c.name,
            }
        )

    return JsonResponse({"trainer": trainers})


def return_schedule_info(request):
    schedule = []
    for c in Schedule.objects.all():
        schedule.append(
            {
                "name": c.name,
                "date": c.date,
                "people_limit": c.people_limit,
                "leader": str(c.leader.name),
                "activity": str(c.activity.name),
            }
        )
    return JsonResponse({"schedule": schedule})


def return_news(request):
    news = []
    for c in News.objects.all():
        news.append(
            {
                "name": c.title,
                "text": c.text,
                "date": c.date,
            }
        )
    return JsonResponse({"news": news})


# def return_workouts(request):
#     # return JsonResponse(Workouts.objects.prefetch_related("exercises"), safe=False)
#     return JsonResponse(
#         serializers.serialize("json", Workouts.objects.prefetch_related("exercises")),
#         safe=False,
#     )


# def add_workout(request):
#     workout = Workouts(
#         user_id=request.POST["user_id"],
#         name=request.POST["name"],
#         date=request.POST["date"],
#         length=request.POST["length"],
#         personal_highscores=request.POST["personal_highscores"],
#         exercises=Exercises.objects.get(id=request.POST["exercises"]),
#     )
#     workout.save()
#     return HttpResponse()


# def add_exercise(request):
#     exercise = Exercises(
#         name=request.POST["name"],
#         weight=request.POST["weight"],
#         reps=request.POST["reps"],
#     )
#     exercise.save()
#     return HttpResponse()


def add_client(request):
    client = Clients(
        name=request.POST["name"],
        last_name=request.POST["last_name"],
        password=request.POST["password"],
    )
    client.save()
    return HttpResponse()


def add_schedule(request):
    schedule = Schedule(
        name=request.POST["name"],
        date=request.POST["date"],
        people_limit=request.POST["people_limit"],
        leader=Trainer.objects.get(id=request.POST["leader"]),
        activity=Activities.objects.get(id=request.POST["activity"]),
    )
    schedule.save()
    return HttpResponse()


def add_news(request):
    news = News(
        title=request.POST["title"],
        text=request.POST["text"],
        date=request.POST["date"],
    )
    news.save()
    return HttpResponse()


def add_trainer(request):
    trainer = Trainer(name=request.POST["name"])
    trainer.save()
    return HttpResponse()


def add_activity(request):
    activity = Activities.objects.create(
        name=request.POST.get("name"),
        beginner_friendly=request.POST.get("beginner_friendly")
        if request.POST.get("beginner_friendly") != None
        else False,
        crossfit=request.POST.get("crossfit")
        if request.POST.get("crossfit") != None
        else False,
        general_workout=request.POST.get("general_workout")
        if request.POST.get("general_workout") != None
        else False,
        cardio=request.POST.get("cardio")
        if request.POST.get("cardio") != None
        else False,
        legs=request.POST.get("legs") if request.POST.get("legs") != None else False,
        chest=request.POST.get("chest") if request.POST.get("chest") != None else False,
        shoulders=request.POST.get("shoulders")
        if request.POST.get("shoulders") != None
        else False,
        biceps=request.POST.get("biceps")
        if request.POST.get("biceps") != None
        else False,
        triceps=request.POST.get("triceps")
        if request.POST.get("triceps") != None
        else False,
        is_group=request.POST.get("is_group")
        if request.POST.get("is_group") != None
        else False,
        is_competition=request.POST.get("is_competition")
        if request.POST.get("is_competition") != None
        else False,
    )
    activity.save()
    return HttpResponse()


class WorkoutListView(generics.ListAPIView):
    queryset = Workouts.objects.prefetch_related("exercises")
    serializer_class = WorkoutSeializer
