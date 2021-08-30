from django.db import models
from django.utils.timezone import now

class User(models.Model):
    name = models.CharField(max_length=128,unique=True)
    username = models.CharField(null=True, blank=True,max_length=128,unique=True)
    password = models.CharField(default=1,max_length=20)
    entity = models.IntegerField(default=1)
    status = models.SmallIntegerField(default=1)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Meta:
    db_table = 'User'

