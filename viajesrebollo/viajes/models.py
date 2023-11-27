from django.db import models

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    descripttion = models.TextField()
    price = models.FloatField(blank=False, null=False)
    init_date = models.DateField(auto_now=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, blank=True, null=True)
    loc = models.URLField(blank=True, null=False)

class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class ActivityPackage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model_a.name} - {self.model_b.description}"

class TripPlan(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    