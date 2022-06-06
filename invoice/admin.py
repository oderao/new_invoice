from django.contrib import admin

# Register your models here.

from .models import Invoice,senderAddress,clientAddress,Items

admin.site.register(Invoice)
admin.site.register(senderAddress)
admin.site.register(clientAddress)
admin.site.register(Items)
