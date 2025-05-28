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
        fields = '__all__'

    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


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
        fields = '__all__'

    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'

