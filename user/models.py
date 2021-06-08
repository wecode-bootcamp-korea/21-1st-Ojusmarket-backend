from django.db import models

class User(models.Model) :
    identity    = models.CharField(max_length=20, unique=True, null=False)
    password    = models.CharField(max_length=20, null=False)
    phone       = models.CharField(max_length=15, unique=True, null=False)
    name        = models.CharField(max_length=20, null=False)
    email       = models.CharField(max_length=45, unique=True, null=True)
    address     = models.CharField(max_length=100, null=True)
    piled_point = models.IntegerField(null=True)

    class Meta:
        db_table = 'users'
