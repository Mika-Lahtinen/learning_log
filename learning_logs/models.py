from django.db import models

# Create your models here.
class Topic(models.Model):
    """Themes for learning."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return to the texts"""
        return self.text


class Entry(models.Model):
    """Knowledges on the specified topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return to the texts"""
        return self.text[:50] + "..."