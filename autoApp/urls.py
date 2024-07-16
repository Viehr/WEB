from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryListCreateAPIView, CountryDetailAPIView, CarListCreateAPIView, CarDetailAPIView, PartViewSet


router = DefaultRouter()
router.register(r'parts', PartViewSet)


urlpatterns = [
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryDetailAPIView.as_view(), name='country-detail'),
    path('cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail'),
    path('', include(router.urls)),
]

