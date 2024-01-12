from django.urls import path
from .views import ListingDetails, Listings

urlpatterns = [
    path("<int:pk>/", ListingDetails.as_view(), name="listing_detail"),
    path("", Listings.as_view(), name="listings"),
]
