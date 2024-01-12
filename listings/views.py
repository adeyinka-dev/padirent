from rest_framework import generics, permissions

from .models import Listing
from .serializers import ListingSerializer


class Listings(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
