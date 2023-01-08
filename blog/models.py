from datetime import datetime

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    post_date = models.DateField(default=datetime.today, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title