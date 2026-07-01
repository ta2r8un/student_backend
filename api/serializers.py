from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model=User

        fields=[
            "username",
            "email",
            "password"
        ]

        extra_kwargs={
            "password":{"write_only":True}
        }

    def create(self,data):

        return User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model=Student

        fields="__all__"