from django.db import models
from django.utils import timezone

class Element(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5, unique=True)
    atomic_number = models.IntegerField(unique=True)
    atomic_weight = models.FloatField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='element_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Discovery(models.Model):
    element_name = models.CharField(max_length=100)
    discovered_by = models.CharField(max_length=255, null=True, blank=True)
    discovery_year = models.IntegerField(null=True, blank=True)
    trivia = models.TextField(null=True, blank=True)
    image_filename = models.CharField(max_length=255, default="default.webp")  # ✅ Added image field
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.element_name
