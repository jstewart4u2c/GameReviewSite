from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class Review(models.Model):
    game_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    rating = models.FloatField()
    image = models.ImageField(default='images/none/default.jpg', upload_to='game_images')
    short = models.CharField(max_length=200, default='A Juicy Game Review')
    url = EmbedVideoField(default='https://youtu.be/GhLMEFOBXqo?si=RemdII9VdRmQZ5UL')

    def __str__(self):
        return self.game_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


class Comments(models.Model):
    review = models.ForeignKey(Review, related_name="comments", on_delete=models.CASCADE)


