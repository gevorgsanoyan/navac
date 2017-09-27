from django.contrib import admin
from .models import stockTypes
from .models import stock
from .models import stockPFDates
# Register your models here.

admin.site.register(stockTypes)
admin.site.register(stockPFDates)
admin.site.register(stock)