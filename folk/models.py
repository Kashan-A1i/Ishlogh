from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length = 255, help_text = "The name of the tale,myth, or legend")
    content = models.TextField(help_text = "The full text of the Story here")
    narrator = models.CharField(max_length = 255 , help_text = "The person who told, or remembered the story")
    

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