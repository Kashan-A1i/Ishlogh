from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length = 255, help_text = "The name of the tale,myth, or legend")
    content = models.TextField(help_text = "The full text of the Story here")
    narrator = models.CharField(max_length = 255 , help_text = "The person who told, or remembered the story")
    uploader = models.ForeignKey(User, on_delete=models.CASCADE,related_name="stories",help_text="The user that uploaded this story")
    region = models.CharField(max_length=100, help_text="The region or village this story is from (e.g., Mastuj)")
    audio_recording = models.FileField(
        upload_to = 'audio/stories',
        null = True,
        blank = True,
        help_text = 'Optional voice recording of the story'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Stories"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} (Told by: {self.narrator})"

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    location = models.CharField(max_length=100,blank=True,help_text="e.g. ,Mastuj ,Chitral")
    bio = models.TextField(blank=True, help_text = "A short description about yourself/contributor")
    languages = models.CharField(max_length=100, blank=True, help_text="e.g., Khowar, Urdu")
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()