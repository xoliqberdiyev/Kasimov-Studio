from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from common import models 

admin.site.register(models.Partner)
admin.site.register(models.AboutUs, TranslationAdmin)
admin.site.register(models.Video)
admin.site.register(models.Team, TranslationAdmin)
admin.site.register(models.Gallery)
admin.site.register(models.Service)

class ServiceInline(admin.TabularInline):
    model = models.Service
    extra = 0


@admin.register(models.ServiceCategory)
class ServiceCategoryAdmin(TranslationAdmin):
    inlines = [ServiceInline]
