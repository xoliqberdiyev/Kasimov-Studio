from rest_framework import generics, status
from rest_framework.response import Response

from common import serializers, models


class VideoApiView(generics.ListAPIView):
    serializer_class = serializers.VideoSerializer
    queryset = models.Video.objects.all()


class ServiceCategoryApiView(generics.ListAPIView):
    serializer_class = serializers.ServiceCategorySerializer
    queryset = models.ServiceCategory.objects.all()


class ServiceApiView(generics.GenericAPIView):
    serializer_class = serializers.ServiceSerializer

    def get(self, request, category_id):
        try:
            category = models.ServiceCategory.objects.get(id=category_id)
        except models.ServiceCategory.DoesNotExist:
            return Response({"message": "category not found"}, status=status.HTTP_404_NOT_FOUND)
        services = models.Service.objects.filter(category=category)
        serializer = serializers.ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GallerApiView(generics.ListAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer


class PartnerApiView(generics.ListAPIView):
    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer


class AboutUsApiView(generics.ListAPIView):
    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer


class TeamApiView(generics.ListAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

