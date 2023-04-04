from rest_framework import serializers
from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from pract.models import Workouts, Exercises, Activities, News, Clients
from django.core.validators import validate_email


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


# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""

#     password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label="Password confirmation", widget=forms.PasswordInput
#     )

#     class Meta:
#         model = MyUser
#         fields = ("email", "date_of_birth")

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     disabled password hash display field.
#     """

#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = MyUser
#         fields = ("email", "password", "date_of_birth", "is_active", "is_admin")


# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ("email", "date_of_birth", "is_admin")
#     list_filter = ("is_admin",)
#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         ("Personal info", {"fields": ("date_of_birth",)}),
#         ("Permissions", {"fields": ("is_admin",)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("email", "date_of_birth", "password1", "password2"),
#             },
#         ),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)
#     filter_horizontal = ()


# Now register the new UserAdmin...
# admin.site.register(Clients, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
