from rest_framework import generics, permissions

from .models import Listing
from .permissions import IsAgentOrReadOnly
from .serializers import ListingSerializer


class ListingsView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class Listings(generics.ListCreateAPIView):
    permission_classes = (IsAgentOrReadOnly,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAgentOrReadOnly,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
