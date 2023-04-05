from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# from pract.views import WorkoutListView

urlpatterns = [
    # path("return_client_info/", views.return_client_info, name="return_client_info"),
    # path("admin"),
    path("login/", obtain_auth_token, name="obtain-auth-token"),
    path("register/", views.register, name="register"),
    path("add_workout/", views.add_workout, name="add_workout"),
    # path("add_exercise/", views.add_exercise, name="add_exercise"),
    # path(
    #     "return_activities/",
    #     views.return_activities,
    #     name="return_activities",
    # ),
    # path(
    #     "return_trainer_info/",
    #     views.return_trainer_info,
    #     name="return_trainer_info",
    # ),
    # path(
    #     "return_schedule_info/",
    #     views.return_schedule_info,
    #     name="return_schedule_info",
    # ),
    path(
        "return_news",
        views.return_news,
        name="return_news",
    ),
    path(
        "return_news/<int:since>",
        views.return_news_month,
        name="return_news_month",
    ),
    # path(
    #     "add_client/",
    #     views.add_client,
    #     name="add_client",
    # ),
    # path(
    #     "add_schedule/",
    #     views.add_schedule,
    #     name="add_schedule",
    # ),
    # path(
    #     "add_trainer/",
    #     views.add_trainer,
    #     name="add_trainer",
    # ),
    # path(
    #     "add_news/",
    #     views.add_news,
    #     name="add_news",
    # ),
    path(
        "add_activity/",
        views.add_activity,
        name="add_activity",
    ),
    path(
        "return_exercise_activities",
        views.return_exercise_activities,
        name="return_exercise_activities",
    ),
    path(
        "return_all_activities",
        views.return_all_activities,
        name="return_all_activities",
    ),
    path("return_workouts/", views.return_workouts, name="return_workouts"),
    # path("return_workouts/", views.ReturnWorkouts.get, name="return_workouts"),
    path(
        "return_workouts/<int:year>/<int:month>",
        views.return_selected_workouts,
        name="return_selected_workouts",
    ),
    path(
        "return_workout_years",
        views.return_workout_years,
        name="return_workout_years",
    ),
    path(
        "return_workout_months/<int:year>",
        views.return_workout_months,
        name="return_workout_months",
    ),
]
