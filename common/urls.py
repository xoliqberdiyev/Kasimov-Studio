from django.urls import path 

from common import views

urlpatterns = [
    path('videos/', views.VideoApiView.as_view()),
    path('service_categories/', views.ServiceCategoryApiView.as_view()),
    path('services/<int:category_id>/', views.ServiceApiView.as_view()),
    path('galleries/', views.GallerApiView.as_view()),
    path('partners/', views.PartnerApiView.as_view()),
    path('about_us/', views.AboutUsApiView.as_view()),
    path('team/', views.TeamApiView.as_view()),
]