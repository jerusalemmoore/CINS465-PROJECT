# realtime chat adapted from url:
#https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django
from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class UserInfoModel(models.Model):
    username = models.CharField(max_length=240)
    userpassword = models.CharField(max_length=240)
    email = models.EmailField(max_length=240)

    def __str__(self):
        return "username: " + self.username + " | email: " + self.email + " | password: " + self.userpassword

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # content = models.CharField(max_length=200)
    content = models.CharField(max_length=160)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    timeCreated = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content

class Friend(models.Model):
    users = models.ManyToManyField(User)
    currentUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, currentUser, new_friend):
        friend, created = cls.objects.get_or_create(
            currentUser=currentUser
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, currentUser, new_friend):
        friend, created = cls.objects.get_or_create(
        currentUser=currentUser
        )
        friend.users.remove(new_friend)

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
