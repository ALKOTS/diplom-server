from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework import generics, authentication
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.decorators import permission_classes, api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from pract.serializers import WorkoutSeializer, ActivitySerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
import json
from django.core.serializers.json import DjangoJSONEncoder

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


def return_activities(request):
    activities = Activities.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return JsonResponse(serializer.data, safe=False)


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
                "title": c.title,
                "sub_title": c.sub_title,
                "text": c.text,
                "date": c.date,
                "post_url": c.post_url,
            }
        )
    return JsonResponse({"news": news})


# def return_news_month(request, year, month):
def return_news_month(request, since):
    news = []
    for c in News.objects.all().order_by("-id")[since : since + 10 : -1]:
        # for c in News.objects.filter(Q(date__year=year) & Q(date__month=month)):
        news.append(
            {
                "title": c.title,
                "sub_title": c.sub_title,
                "text": c.text,
                "date": c.date,
                "post_url": c.post_url,
            }
        )
    news = news[::-1]

    return JsonResponse({"news": news})


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
        sub_title=request.POST["sub_title"],
        text=request.POST["text"],
        date=request.POST["date"],
        post_url=request.POST["post_url"],
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


# class WorkoutListView(generics.ListAPIView):
#     queryset = Workouts.objects.prefetch_related("exercises")
#     serializer_class = WorkoutSeializer


def return_workouts_basic(request):
    workouts = Workouts.objects.filter(user=request.user)
    return workouts


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def return_selected_workouts(request, year, month):
    if request.method == "GET":
        try:
            workouts = (
                return_workouts_basic(request)
                .filter(Q(year=year) & Q(month=month))
                # Workouts.objects.filter(Q(year=year) & Q(month=month))
                .order_by("year")
                .order_by("month")
                .order_by("day")
            )
            serializer = WorkoutSeializer(workouts, many=True)
            return JsonResponse({"workouts": serializer.data}, safe=False)
        except Workouts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # workouts = Workouts.objects.all()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def return_workouts(request):
    # workouts = Workouts.objects.filter(user=request.user)
    # print(request.user)
    workouts = return_workouts_basic(request)  # Workouts.objects.all()
    serializer = WorkoutSeializer(workouts, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def return_workout_years(request):
    try:
        years = list(
            map(
                lambda d: d["year"],
                list(
                    return_workouts_basic(request)
                    .order_by()
                    .values("year")
                    .distinct()
                    .values(
                        "year"
                    )  # Workouts.objects.order_by().values("year").distinct().values("year")
                ),
            )
        )
        # years.reverse()
        return JsonResponse({"years": years})
    except Workouts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def return_workout_months(request, year):
    months = list(
        map(
            lambda d: d["month"],
            list(
                return_workouts_basic(request)
                .filter(Q(year=year))  # Workouts.objects.filter(Q(year=year))
                .order_by("month")
                .distinct()
                .values("month")
            ),
        )
    )
    months.reverse()

    print(months)
    return JsonResponse({"months": months})
