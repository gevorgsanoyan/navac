from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

# Create your models here.
class portfolioManager(models.Model):
    pmName = models.CharField(max_length=250)
    pmAutorPerson = models.CharField(max_length=250)
    pmPhone = models.CharField(max_length=50)
    pmAddress = models.CharField(max_length=500)
    pmEmail = models.CharField(max_length=50)
    pmCountry = CountryField()
    sgroup = models.ForeignKey('auth.Group')

    def __str__(self):
        return self.pmName + " (" + self.sgroup.name + ")"


class pmUsers(models.Model):
    pmName =  models.CharField(max_length=150)
    pm = models.ForeignKey(portfolioManager)
    sUser = models.ForeignKey('auth.User')
    transMaxLimit = models.DecimalField(max_digits=10, decimal_places=2)
    pmPosition =  models.CharField(max_length=150)
    uTel = models.CharField(max_length=50)
    uEmail = models.CharField(max_length=50)
    cDate = models.DateField(default=timezone.now())

    def __str__(self):
        return self.pmName