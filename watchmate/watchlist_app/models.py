from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

# Create your models here.
class WatchList(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    active=models.BooleanField(default=True)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
    created=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
    
class Review(models.Model):
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')
    description=models.CharField(max_length=200,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.name