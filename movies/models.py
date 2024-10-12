from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    pub_date = models.DateTimeField("date published")


class Gener(models.Model):
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)   