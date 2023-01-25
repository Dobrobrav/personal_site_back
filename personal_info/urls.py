from django.urls import path
from .views import *

urlpatterns = [
    path('main_info/', (MainInfoAPIView.as_view())),
    path('contact_details/', (ContactDetailsAPIView.as_view())),
    path('interests/', (InterestsAPIView.as_view())),
    path('certificates/', (CertificatesAPIView.as_view())),
    path('footer_info/', (FooterInfoAPIView.as_view()))
]


