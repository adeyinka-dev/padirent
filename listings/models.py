from django.db import models
from django.conf import settings


class Listing(models.Model):
    # agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/", blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=[("available", "Available"), ("rented", "Rented")],
        default="available",
    )

    def __str__(self):
        return f"{self.title} - {self.status}"
