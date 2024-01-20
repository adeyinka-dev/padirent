from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny

from .models import Listing
from .permissions import IsAgentOrReadOnly
from .serializers import ListingSerializer, UserSerializer


class ListingViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    # If user is not authenticated, remove modification from view
    # def get_permissions(self):
    #     if self.action in ["create"]:
    #         permission_classes = [AllowAny]
    #     if self.action in ["list", "retrieve"]:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [AllowAny]
    #     return [permission() for permission in permission_classes]


class AgentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
