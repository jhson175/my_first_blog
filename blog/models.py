from django.db import models
<<<<<<< HEAD
=======

# Create your models here.

from django.db import models
>>>>>>> 5568dec7fed51abab79184df9bbcb0d5ad3ae788
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
<<<<<<< HEAD
        return self.title
=======
        return self.title
        
        
>>>>>>> 5568dec7fed51abab79184df9bbcb0d5ad3ae788
