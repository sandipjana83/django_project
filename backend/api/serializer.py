from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet, Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "bio",
            "profile_pic",
        ]

class TweetSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"