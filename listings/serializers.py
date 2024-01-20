from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "description",
            "price",
            "location",
            "image",
            "added_on",
            "updated_at",
            "status",
        )
        model = Listing


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")
