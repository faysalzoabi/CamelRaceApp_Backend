from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    image = models.ImageField(upload_to='profile_image', blank=True)
    position = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    symbols = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()


class Camel(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='camels'
    )

    def __str__(self):
        return f"{self.age} | {self.name} | {self.user}"


class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='events'
    )
    eventname = models.CharField(max_length=100)
    eventdate = models.DateTimeField(auto_now_add=True)
    season = models.ForeignKey(
        to='api.Season',
        on_delete=models.CASCADE,
        related_name="events"
    )
    camel = models.ForeignKey(
        to='api.Camel',
        on_delete=models.CASCADE,
        related_name="events"
    )
    eventRound = models.IntegerField()
    age = models.CharField(max_length=100)
    points = models.IntegerField()
    rank = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.eventname}"


##### To include later in the Database Model ####

# class Round(models.Model):
#     round_number=models.IntegerField()
#     event=models.ForeignKey(
#         to='api.Event',
#         on_delete=models.CASCADE,
#         related_name="rounds"
#     )
#     position=models.IntegerField()
#     points=models.IntegerField()

#     def __str__(self):
#         return f'{self.round_number}'

# class Video_Links(models.Model):
#     video_url=models.CharField(max_length=100)
#     round=models.ForeignKey(
#         to='api.Round',
#         on_delete=models.CASCADE,
#         related_name="video_links"
#     )
