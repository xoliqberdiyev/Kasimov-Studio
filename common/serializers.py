from rest_framework import serializers

from common import models 


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = [
            'id', 'video'
        ]

    
class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceCategory
        fields = [
            'id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image', 'video'
        ]

    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = [
            'id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image', 'category'
        ]



class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = '__all__'

    
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutUs
        fields = [
            'id', 'title_uz', 'title_ru', 'image'
        ]

    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = [
            'id', 'full_name', 'position'
        ]

