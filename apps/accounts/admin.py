from django.contrib import admin
from .models import User, PropertyManager, Tenant

admin.site.register(User)
admin.site.register(PropertyManager)
admin.site.register(Tenant) 