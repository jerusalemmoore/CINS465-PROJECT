from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.UserInfoModel)
admin.site.register(models.PostModel)
admin.site.register(models.Friend)
