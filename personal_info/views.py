from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils import DebugQueryMixin
from .serializers import *
from .models import *


class MainInfoAPIView(generics.RetrieveAPIView):
    serializer_class = MainInfoSerializer

    def get_object(self):
        profile = Profile.objects.select_related('department') \
            .get(pk=self.kwargs[self.lookup_field])
        return profile


# need to check if serializer and address match
class ContactDetailsAPIView(DebugQueryMixin, generics.RetrieveAPIView):
    serializer_class = ContactDetailsSerializer

    def get_object(self):
        profile = Profile.objects \
            .select_related('contact_details', 'office__address') \
            .get(pk=self.kwargs[self.lookup_field])
        return profile


class InterestsAPIView(generics.ListAPIView):
    serializer_class = InterestsSerializer

    def get_queryset(self):
        profile = Profile.objects.get(pk=self.kwargs[self.lookup_field])
        return profile.interests.all()


class CertificatesAPIView(generics.ListAPIView):
    serializer_class = CertificatesSerializer

    def get_queryset(self):
        profile = Profile.objects.get(pk=self.kwargs[self.lookup_field])
        return profile.certificates.all()


class FooterInfoAPIView(generics.RetrieveAPIView):
    serializer_class = FooterSerializer

    def get_object(self):
        profile = Profile.objects.select_related('contact_details') \
            .get(pk=self.kwargs[self.lookup_field])
        return profile.contact_details
