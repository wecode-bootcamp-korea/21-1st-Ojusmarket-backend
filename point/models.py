from django.db import models

from user.models import User

class Point(models.Model):
    new_client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='new')
    old_client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='old')
    date       = models.DateTimeField()

    class Meta:
        db_table = 'points'
