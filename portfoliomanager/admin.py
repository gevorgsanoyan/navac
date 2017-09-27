from django.contrib import admin
from .models import portfolioManager
from .models import pmUsers
# Register your models here.
admin.site.register(portfolioManager)
admin.site.register(pmUsers)