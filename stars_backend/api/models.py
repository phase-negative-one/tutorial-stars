from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    star_rating = models.FloatField()


def __str__(self):
    return '%s %s' % (self.title, self.description)