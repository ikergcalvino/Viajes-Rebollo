from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(blank=False, null=False)
    init_date = models.DateField(auto_now=False, blank=False, null=True)
    end_date = models.DateField(auto_now=False, blank=False, null=True)
    loc = models.URLField(blank=True, null=False)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    activities = models.ManyToManyField(Activity, blank=True)

    def __str__(self):
        return self.name


class TripPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_creation = models.DateField(auto_now_add=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customized_activities = models.ManyToManyField(Activity, blank=True)

    def total_price(self):
        return sum(activity.price for activity in self.customized_activities.all())

    def __str__(self):
        return self.name
