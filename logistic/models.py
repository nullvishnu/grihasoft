from django.db import models
from django.utils.timezone import now

class City(models.Model):
    name = models.CharField(max_length=36,unique=True)
    part = models.CharField(max_length=36)
    status = models.SmallIntegerField(default=1)
    create_by = models.IntegerField()
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Meta:
    db_table = 'City'

class Zone(models.Model):
    source = models.IntegerField()
    destination = models.IntegerField()
    zone = models.CharField(max_length=8)
    status = models.SmallIntegerField(default=1)
    create_by = models.IntegerField()
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Meta:
    db_table = 'Zone'

class Rate(models.Model):
    weight = models.FloatField(max_length=16)
    zone = models.CharField(max_length=16)
    rate = models.FloatField(max_length=16)
    status = models.SmallIntegerField(default=1)
    create_by = models.IntegerField()
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Meta:
    db_table = 'Rate'

class Logistics(models.Model):
    fromcity= models.ForeignKey(City,related_name='Logistics_fromcity',on_delete=models.CASCADE)
    tocity = models.ForeignKey(City,on_delete=models.CASCADE)
    zone = models.CharField(max_length=16)
    rate = models.FloatField(max_length=16)
    weight = models.FloatField(default=1)
    status = models.SmallIntegerField(default=1)
    create_by = models.IntegerField()
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Meta:
    db_table = 'Logistics'
