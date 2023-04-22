from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework import generics, authentication, filters
from rest_framework.permissions import (
    BasePermission,
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    SAFE_METHODS,
)
from rest_framework.decorators import permission_classes, api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from pract.serializers import (
    WorkoutSeializer,
    ActivitySerializer,
    NewsSerializer,
    RegistrationSerializer,
    ScheduleSerializer,
    AppointmentsSerializer,
    ClientSerializer,
)
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
import json
from django.core.serializers.json import DjangoJSONEncoder

from pract.models import (
    Appointments,
    Clients,
    Activities,
    Schedule,
    Trainer,
    News,
    Workouts,
    Exercises,
)

from datetime import date, timedelta

# from models import get_clients

# Create your views here.
# def return_client_info(request):
#     clients = []
#     # Clients.objects.raw("SELECT * FROM clients", translations=name_map)
#     for c in Clients.objects.raw("SELECT * FROM clients"):
#         clients.append(
#             {"name": c.name, "last_name": c.last_name, "password": c.password}
#         )

#     return JsonResponse({"client": clients})


# def return_activities(request):
#     activities = Activities.objects.all()
#     serializer = ActivitySerializer(activities, many=True)
#     return JsonResponse(serializer.data, safe=False)


# def return_trainer_info(request):
#     trainers = []
#     for c in Trainer.objects.all():
#         trainers.append(
#             {
#                 "id": c.id,
#                 "name": c.name,
#             }
#         )

#     return JsonResponse({"trainer": trainers})


@api_view(["GET"])
@permission_classes([IsAdminUser])
def return_schedule(request):
    schedule = Schedule.objects.all()
    serializer = ScheduleSerializer(schedule, many=True)
    return JsonResponse({"schedule": serializer.data})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def return_schedule_week(request):
    current_week, offset = (
        date.fromisoformat(request.data["now"]),
        # - timedelta(days=date.fromisoformat(request.data["now"]).weekday()),
        request.data["offset"],
    )
    print(offset)
    weekday, next_weekday = current_week + timedelta(
        7 * offset
    ), current_week + timedelta(7 * offset + 7)

    print(weekday, next_weekday)
    schedule = (
        Schedule.objects.filter(date__range=[weekday, next_weekday])
        .order_by("date")
        .order_by("startTime")
    )
    print(schedule)

    # ss = []
    # for c in Appointments.objects.filter(
    #     Q(client=request.user) & Q(schedule_position__date__gte=weekday)
    # ).only("schedule_position"):
    #     ss.append(ScheduleSerializer(c.schedule_position)["id"].value)

    # print(ss)
    serializer = ScheduleSerializer(schedule, many=True)

    return JsonResponse(
        {"schedule": serializer.data, "weekday": weekday, "next_weekday": next_weekday}
    )


@api_view(["GET"])
@permission_classes([IsAdminUser])
def return_news(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return JsonResponse({"news": serializer.data})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def check_for_appointment(request):
    return JsonResponse(
        {
            "enrolled": Appointments.objects.filter(
                Q(client=request.user) & Q(schedule_position__id=request.data["id"])
            ).count()
        }
    )  # AppointmentsSerializer(ss, many=True).data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def return_news_month(request, since):
    print(since)

    news = News.objects.order_by("-id")[since : since + 10 : 1]
    serializer = NewsSerializer(news, many=True)

    return JsonResponse({"news": serializer.data})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def return_appointments(request):
    appointments = Appointments.objects.filter(
        Q(client=request.user) & Q(schedule_position__date__gte=request.data["date"])
    ).order_by("schedule_position__date")
    serializer = AppointmentsSerializer(appointments, many=True)

    return JsonResponse({"appointments": serializer.data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def return_client(request):
    client = Clients.objects.filter(login=request.user)
    serializer = ClientSerializer(client, many=True)

    return JsonResponse({"client": serializer.data})


# def add_client(request):
#     client = Clients(
#         name=request.POST["name"],
#         last_name=request.POST["last_name"],
#         password=request.POST["password"],
#     )
#     client.save()
#     return HttpResponse()


# def add_schedule(request):
#     schedule = Schedule(
#         name=request.POST["name"],
#         date=request.POST["date"],
#         people_limit=request.POST["people_limit"],
#         leader=Trainer.objects.get(id=request.POST["leader"]),
#         activity=Activities.objects.get(id=request.POST["activity"]),
#     )
#     schedule.save()
#     return HttpResponse()


# def add_news(request):
#     news = News(
#         title=request.POST["title"],
#         sub_title=request.POST["sub_title"],
#         text=request.POST["text"],
#         date=request.POST["date"],
#         post_url=request.POST["post_url"],
#     )
#     news.save()
#     return HttpResponse()


# def add_trainer(request):
#     trainer = Trainer(name=request.POST["name"])
#     trainer.save()
#     return HttpResponse()


@api_view(["POST"])
@permission_classes([IsAdminUser])
def add_activity(request):
    activity = Activities.objects.create(
        name=request.POST.get("name"),
        beginner_friendly=request.POST.get("beginner_friendly"),
        crossfit=request.POST.get("crossfit"),
        general_workout=request.POST.get("general_workout"),
        cardio=request.POST.get("cardio"),
        legs=request.POST.get("legs"),
        chest=request.POST.get("chest"),
        shoulders=request.POST.get("shoulders"),
        biceps=request.POST.get("biceps"),
        triceps=request.POST.get("triceps"),
        is_group=request.POST.get("is_group"),
        is_competition=request.POST.get("is_competition"),
        is_exercise=request.POST.get("is_exercise"),
    )
    activity.save()
    return HttpResponse()


# class WorkoutListView(generics.ListAPIView):
#     queryset = Workouts.objects.prefetch_related("exercises")
#     serializer_class = WorkoutSeializer
def add_exercise(exercise_list, workout_id):
    # exercise_list = json.loads(exercise_list)
    # print(exercise_list)

    for exercise in exercise_list:
        # print(exercise)
        Exercises(
            weight=exercise["weight"],
            reps=exercise["reps"],
            workout_id=Workouts.objects.get(pk=workout_id),
            activity=Activities.objects.get(pk=exercise["activity"]),
        ).save()
    return HttpResponse()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_workout(request):
    # print(request.data)
    year, month, day = request.data["date"].split(" ")
    workout = Workouts(
        user=request.user,
        name=request.data["name"],
        year=year,
        month=month,
        day=day,
        startTime=request.data["startTime"],
        endTime=request.data["endTime"],
        personal_highscores_amount=0,
    )
    workout.save()
    add_exercise(
        request.data["exercises"],
        workout.id,
    )
    return Response(data={"data": "Success"}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_workout(request):
    Workouts.objects.filter(id=request.data["id"]).delete()
    return Response(data={"data": "Success"}, status=status.HTTP_200_OK)


# Response(data={"response": workout.id}, status=status.HTTP_200_OK)


def return_activities():
    activities = Activities.objects.all()
    return activities


@api_view(["GET"])
@permission_classes([IsAdminUser])
def return_all_activities(request):
    activities = return_activities()
    serializer = ActivitySerializer(activities, many=True)
    return JsonResponse({"activities": serializer.data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def return_exercise_activities(request):
    activities = return_activities().filter(Q(is_exercise=True)).order_by("name")
    serializer = ActivitySerializer(activities, many=True)
    return JsonResponse({"exercises": serializer.data})


class ActivitiesAPIView(generics.ListCreateAPIView):
    api_view = ["GET"]
    permission_classes = [IsAuthenticated]
    search_fields = ["name"]
    filter_backends = (filters.SearchFilter,)
    queryset = return_activities().filter(Q(is_exercise=True)).order_by("name")
    serializer_class = ActivitySerializer


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
                    .distinct()
                    .values(
                        "year"
                    )  # Workouts.objects.order_by().values("year").distinct().values("year")
                ),
            )
        )
        years.sort()
        years.reverse()
        print(years)
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
    return JsonResponse({"months": months})


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        client = serializer.save()
        data["response"] = "Success"

    else:
        data = {"response": "Error", "Errors": serializer.errors}

    print(data)
    return Response(data, status=status.HTTP_200_OK)

    # return Response(status=status.HTTP_200_OK)
