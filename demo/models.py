from django.db import models

# Create your models here.
class Deals(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    original_price = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deals'

