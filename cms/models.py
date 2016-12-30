from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Track(models.Model):
    user = models.ForeignKey(User, related_name='tracks')
    distance = models.FloatField()
    date = models.DateTimeField(default=datetime.now)