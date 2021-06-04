from django.contrib import admin

from .models import Sender, Receiver, Package
# Register your models here.


admin.site.register([Sender, Receiver, Package])
