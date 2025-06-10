from modeltranslation.translator import register, TranslationOptions

from common import models 


@register(models.AboutUs)
class AboutUsTranslation(TranslationOptions):
    fields = ['title']    


@register(models.ServiceCategory)
class ServiceCategoryTranslation(TranslationOptions):
    fields = ['title', 'description']    


@register(models.Service)
class ServiceTranslation(TranslationOptions):
    fields = ['title', 'description']    


@register(models.Team)
class TeamTranslation(TranslationOptions):
    fields = ['position']    
