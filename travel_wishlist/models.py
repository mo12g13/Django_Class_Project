from django.db import models
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    place_review = models.TextField()

    def __str__(self):
        return '{} visited? {}'.format(self.name, self.visited)