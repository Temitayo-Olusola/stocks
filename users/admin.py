from django.contrib import admin
from .models import CustomUser, Details, Profile, Profit_loss
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Details)
admin.site.register(Profit_loss)