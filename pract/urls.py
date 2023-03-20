from django.urls import path
from . import views
from pract.views import WorkoutListView

urlpatterns = [
    path("return_client_info/", views.return_client_info, name="return_client_info"),
    # path("admin"),
    path(
        "return_activities_info/",
        views.return_activities_info,
        name="return_activities_info",
    ),
    path(
        "return_trainer_info/",
        views.return_trainer_info,
        name="return_trainer_info",
    ),
    path(
        "return_schedule_info/",
        views.return_schedule_info,
        name="return_schedule_info",
    ),
    path(
        "add_client/",
        views.add_client,
        name="add_client",
    ),
    path(
        "add_schedule/",
        views.add_schedule,
        name="add_schedule",
    ),
    path(
        "add_trainer/",
        views.add_trainer,
        name="add_trainer",
    ),
    path(
        "add_activity/",
        views.add_activity,
        name="add_activity",
    ),
    path("return_workouts/", WorkoutListView.as_view(), name="pract-workout-list"),
]
