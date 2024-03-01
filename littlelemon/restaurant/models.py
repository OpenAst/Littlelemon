from django.db import models

class Booking(models.Model):
    id = models.IntegerField(default=5, primary_key=True)
    name = models.CharField(max_length=255)
    no_of_quests = models.IntegerField()
    bookingDate = models.DateTimeField(verbose_name="Created at")

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)
    