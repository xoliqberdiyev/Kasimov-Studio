from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from common import models 


admin.site.register(models.ServiceCategory)
admin.site.register(models.Service)
admin.site.register(models.Gallery)
admin.site.register(models.Partner)
admin.site.register(models.AboutUs)
admin.site.register(models.Video)
admin.site.register(models.Team)
