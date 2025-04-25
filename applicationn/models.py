from django.db import models

class Movie(models.Model):
    moviename=models.CharField(max_length=30)
    lan=models.CharField(max_length=20)
    rating=models.FloatField()
    about=models.TextField()
    date=models.DateField()
    movieimg=models.ImageField()
    username=models.CharField(max_length=40)
    email=models.EmailField()


    def __str__(self):
      return self.moviename



