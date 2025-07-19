from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from common import models 

admin.site.register(models.ServiceCategory, TranslationAdmin)
admin.site.register(models.Service, TranslationAdmin)
admin.site.register(models.Partner)
admin.site.register(models.AboutUs, TranslationAdmin)
admin.site.register(models.Video)
admin.site.register(models.Team, TranslationAdmin)


@admin.register(models.Gallery)
class GalaryAdmin(admin.ModelAdmin):
    ...