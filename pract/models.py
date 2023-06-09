from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    User,
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class Activities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    beginner_friendly = models.BooleanField(default=False)
    crossfit = models.BooleanField(default=False)
    general_workout = models.BooleanField(default=False)
    cardio = models.BooleanField(default=False)
    back = models.BooleanField(default=False)
    legs = models.BooleanField(default=False)
    chest = models.BooleanField(default=False)
    shoulders = models.BooleanField(default=False)
    biceps = models.BooleanField(default=False)
    triceps = models.BooleanField(default=False)
    abs = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    is_competition = models.BooleanField(default=False)
    is_exercise = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = "activities"

    def __str__(self) -> str:
        return self.name


class ClientManager(BaseUserManager):
    def create_user(self, login, username, last_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        client = Clients(
            login=login,
            username=username,
            last_name=last_name,
            email=self.normalize_email(email),
        )

        client.set_password(password)
        client.save()
        return client

    def create_superuser(self, login, username, last_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        client = Clients(
            login=login,
            username=username,
            last_name=last_name,
            email=self.normalize_email(email),
        )

        client.set_password(password)
        client.is_admin = True
        client.save()
        return client


class Clients(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    login = models.CharField(unique=True, max_length=100, null=True)
    username = models.CharField(default="default_name", max_length=100)
    last_name = models.CharField(default="default_last_name", max_length=100)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        default="defaultEmail@kursa4.com",
    )

    USERNAME_FIELD = "login"

    REQUIRED_FIELDS = ["username", "last_name", "email"]

    objects = ClientManager()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.login

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return self.is_admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

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
    date = models.DateField(null=True)
    startTime = models.TimeField(null=True)
    endTime = models.TimeField(null=True)
    people_limit = models.IntegerField(default=20)
    people_enlisted = models.IntegerField(default=0)
    place = models.CharField(max_length=100, null=True)
    # is_free = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    leader = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        to_field="id",
        null=True,  # default=1
    )
    description = models.CharField(null=True, max_length=1000)
    activity = models.ForeignKey(
        Activities, on_delete=models.CASCADE, to_field="id", default=1
    )

    def __str__(self):
        return str(str(self.activity) + " " + str(self.date))

    class Meta:
        managed = True
        db_table = "schedule"


class Appointments(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        Clients, on_delete=models.CASCADE, to_field="id", default=1
    )
    schedule_position = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, to_field="id", default=1
    )

    class Meta:
        managed = True
        db_table = "appointments"

    def __str__(self) -> str:
        return str(self.client)


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
    user = models.ForeignKey(Clients, on_delete=models.CASCADE, default=1)
    name = models.CharField(blank=True, null=True, max_length=100)
    year = models.IntegerField(default=2001, null=True)
    month = models.IntegerField(default=1, null=True)
    day = models.CharField(default=1, null=True, max_length=100)
    startTime = models.TimeField(default="0:00:00")
    endTime = models.TimeField(default="1:00:00")
    length = models.CharField(default=1, null=True, max_length=100)
    personal_highscores_amount = models.CharField(
        default=0, null=True, max_length=100
    )  # TODO

    class Meta:
        managed = True
        db_table = "workouts"

    def __str__(self) -> str:
        return str(self.name)


class Exercises(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.CharField(default=0, null=True, max_length=100)
    reps = models.CharField(default=0, null=True, max_length=100)
    workout_id = models.ForeignKey(
        Workouts,
        on_delete=models.CASCADE,
        null=True,
        related_name="exercises",
    )

    activity = models.ForeignKey(
        Activities,
        on_delete=models.SET_NULL,
        null=True,
        related_name="activity",
    )

    class Meta:
        managed = True
        db_table = "exercises"

    def __str__(self) -> str:
        return str(self.workout_id)


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
