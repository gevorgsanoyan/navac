from django.contrib import admin
from .models import cashFlow
from .models import banks
from .models import bankAccount
from .models import cfTransactTypes
# Register your models here.

admin.site.register(cashFlow)
admin.site.register(banks)
admin.site.register(bankAccount)
admin.site.register(cfTransactTypes)