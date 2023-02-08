from django.urls import path
from .views import *

urlpatterns = [
    path('main_info/<int:pk>/', (MainInfoAPIView.as_view())),
    path('contact_details/<int:pk>/', (ContactDetailsAPIView.as_view())),
    path('interests/<int:pk>/', (InterestsAPIView.as_view())),
    path('certificates/<int:pk>/', (CertificatesAPIView.as_view())),
    path('footer_info/<int:pk>/', (FooterInfoAPIView.as_view()))
]


