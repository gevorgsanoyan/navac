from django.contrib.admin import models
from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone

# Create your models here.
class stockTypes(models.Model):
    stockType = models.CharField(max_length=50)
    sTypeDescr = models.CharField(max_length=200)

    def __str__(self):
        return self.stockType


class stock(models.Model):
    stockName = models.CharField(max_length=50)
    issuer = models.CharField(max_length=100)
    NYSEexchCode = models.CharField(max_length=50)
    NASDAQexchCode = models.CharField(max_length=50)
    otherExchCode = models.CharField(max_length=50)
    sType = models.ForeignKey(stockTypes)
    nominalAndCurrency = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    issuedPr = models.DecimalField(max_digits=10, decimal_places=4)
    cuponsCount = models.IntegerField()
    cuponPr = models.DecimalField(max_digits=10, decimal_places=4)
    accruedInterest = models.DecimalField(max_digits=10, decimal_places=2)
    imUser = models.ForeignKey('auth.User')

    def __str__(self):
        return self.stockName


class stockPFDates(models.Model):
    stockId = models.ForeignKey(stock)
    pfDate = models.DateField(default=timezone.now())

    def __str__(self):
        return self.stockId.stockName + " " + str(self.pfDate)