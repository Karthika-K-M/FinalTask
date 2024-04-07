from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    CATEGORY_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Romance', 'Romance'),
        # Add more choices as needed
    ]
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    releasedate = models.DateField()
    actors = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    trailer = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Review(models.Model):
    movie = models.ForeignKey(Movies, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
    return   self.title
