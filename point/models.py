from django.db import models

from user.models import User

class Point(models.Model):
    new_client_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='new')
    old_client_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='old')
    created_at    = models.DateTimeField(auto_now_add=True)
    point         = models.IntegerField(null=True)
    class Meta:
        db_table = 'points'
