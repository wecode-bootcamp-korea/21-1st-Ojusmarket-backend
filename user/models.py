from django.db import models

class User(models.Model) :

    identity = models.CharField(max_length=45, unique=True, null=False)
    password = models.CharField(max_length=45, null=False)
    phone    = models.CharField(max_length=11, unique=True, null=False)
    name     = models.CharField(max_length=45, null=False)
    email    = models.CharField(max_length=45, unique=True, null=False)
    address  = models.TextField(null=False)

    class Meta:
        db_table = 'users'
        
        
