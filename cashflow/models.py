from django.db import models
from portfoliomanager.models import portfolioManager
from djmoney.models.fields import MoneyField
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your models here.

class banks(models.Model):
    bankName = models.CharField(max_length=250)
    bankAddress = models.CharField(max_length=500)
    contactTel = models.CharField(max_length=50)

    def __str__(self):
        return self.bankName

class bankAccount(models.Model):
    baName = models.CharField(max_length=250)
    bankId = models.ForeignKey(banks, on_delete=models.CASCADE)
    pmId = models.ForeignKey(portfolioManager, on_delete=models.CASCADE)
    currency = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.baName + " of " + self.pmId.pmName

class cfTransactTypes(models.Model):
    transactType =  models.CharField(max_length=60)
    transactTypeFL = models.CharField(max_length=60)
    transactSign = models.IntegerField(default=1)# 1 or -1

    def __str__(self):
        return self.transactType + "(" + str(self.transactSign)[:1] + ")"


class cashFlow(models.Model):
    cfDate = models.DateField(default=timezone.now())
    currency = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    pmId = models.ForeignKey(portfolioManager, on_delete=models.CASCADE)
    baId = models.ForeignKey(bankAccount, on_delete=models.CASCADE)
    transType = models.ForeignKey(cfTransactTypes)
    cfAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.cfDate) + str(self.pmId_id)

    def save(self):
        trans = cfTransactTypes.objects.filter(pk=self.transType_id).values()
        for t in trans:
            s = int(t['transactSign'])

        self.cfAmount = float(self.currency) * s
        #self.cfAmount = self.cfAmount * s
        super(cashFlow, self).save()







