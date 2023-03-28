# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    beginner_friendly = models.BooleanField(null=True, default=False)
    crossfit = models.BooleanField(null=True, default=False)
    general_workout = models.BooleanField(null=True, default=False)
    cardio = models.BooleanField(null=True, default=False)
    legs = models.BooleanField(null=True, default=False)
    chest = models.BooleanField(null=True, default=False)
    shoulders = models.BooleanField(null=True, default=False)
    biceps = models.BooleanField(null=True, default=False)
    triceps = models.BooleanField(null=True, default=False)
    is_group = models.BooleanField(null=True, default=False)
    is_competition = models.BooleanField(null=True, default=False)

    class Meta:
        managed = True
        db_table = "activities"


class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    last_name = models.CharField(blank=True, null=True, max_length=100)
    password = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        managed = True
        db_table = "clients"


class Trainer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        managed = True
        db_table = "trainer"


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    date = models.DateField(blank=True, null=True)
    people_limit = models.IntegerField(blank=True, null=True)
    leader = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, to_field="id", null=True
    )
    activity = models.ForeignKey(
        Activities, on_delete=models.CASCADE, to_field="id", null=True
    )

    class Meta:
        managed = True
        db_table = "schedule"


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, null=True, max_length=100)
    sub_title = models.CharField(blank=True, null=True, max_length=100)
    text = models.CharField(blank=True, null=True, max_length=500)
    date = models.DateField(blank=True, null=True)
    post_url = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        managed = True
        db_table = "news"


class Workouts(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=0, null=True)  # TODO connect to users db
    name = models.CharField(blank=True, null=True, max_length=100)
    # date = models.DateField(null=True)
    year = models.IntegerField(default=2001, null=True)
    month = models.IntegerField(default=1, null=True)
    day = models.CharField(default=1, null=True, max_length=100)
    length = models.CharField(default=1, null=True, max_length=100)
    personal_highscores_amount = models.CharField(
        default=0, null=True, max_length=100
    )  # TODO

    class Meta:
        managed = True
        db_table = "workouts"

    def __str__(self) -> str:
        return self.name


class Exercises(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    weight = models.CharField(default=0, null=True, max_length=100)
    reps = models.CharField(default=0, null=True, max_length=100)
    workout_id = models.ForeignKey(
        Workouts,
        on_delete=models.CASCADE,
        null=True,
        default=0,
        related_name="exercises",
    )

    class Meta:
        managed = True
        db_table = "exercises"


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = "auth_group"


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = "auth_group_permissions"
#         unique_together = (("group", "permission"),)


# class AuthPermission(models.Model):
#     content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#     name = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = "auth_permission"
#         unique_together = (("content_type", "codename"),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     first_name = models.CharField(max_length=150)

#     class Meta:
#         managed = False
#         db_table = "auth_user"


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = "auth_user_groups"
#         unique_together = (("user", "group"),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = "auth_user_user_permissions"
#         unique_together = (("user", "permission"),)


# class DjangoAdminLog(models.Model):
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey(
#         "DjangoContentType", models.DO_NOTHING, blank=True, null=True
#     )
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     action_time = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = "django_admin_log"


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = "django_content_type"
#         unique_together = (("app_label", "model"),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = "django_migrations"


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = "django_session"
