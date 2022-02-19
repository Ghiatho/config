from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):              # this is for admin to show nice titles not object() junk title .... add to mnwho
        return self.text[:50]