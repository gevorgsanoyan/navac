from django.db import models
from django.utils import timezone

# Create your models here.

class portfolio(models.Model):
    tDate = models.DateField(default=timezone.now())