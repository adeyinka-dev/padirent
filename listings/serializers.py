from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "agent",
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
