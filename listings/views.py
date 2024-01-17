from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Listing
from .permissions import IsAgentOrReadOnly
from .serializers import ListingSerializer, UserSerializer


# class ListingsView(generics.ListAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAgentOrReadOnly,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class AgentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
