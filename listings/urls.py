from django.urls import path
from .views import ListingDetails, Listings, ListingsView

urlpatterns = [
    path("<int:pk>/", ListingDetails.as_view(), name="listing_detail"),
    path("", Listings.as_view(), name="listings"),
    path("listings/", ListingsView.as_view(), name="listings_list"),
]
