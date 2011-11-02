from django.db import models

# Create your models here.
class KeyDate(models.Model):
    name        = models.CharField(max_length = 32)
    description = models.CharField(max_length = 320)
    event_date  = models.DateField()
