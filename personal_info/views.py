from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utils import DebugQueryMixin
from .serializers import *
from .models import *


class MainInfoAPIView(DebugQueryMixin, generics.RetrieveAPIView):
    serializer_class = MainInfoSerializer

    def get_object(self):
        profile_id = self.request.data['profile_id']
        # profile_id = 1
        profile = Profile.objects.select_related('department') \
            .get(pk=profile_id)
        return profile


class ContactDetailsAPIView(DebugQueryMixin, generics.RetrieveAPIView):
    serializer_class = ContactDetailsSerializer

    def get_object(self):
        profile_id = self.request.data['profile_id']
        profile = Profile.objects \
            .select_related('contact_details', 'office__address') \
            .get(pk=profile_id)
        return profile


class InterestsAPIView(generics.ListAPIView):
    serializer_class = InterestsSerializer

    def get_queryset(self):
        profile_id = self.request.data['profile_id']
        profile = Profile.objects.get(pk=profile_id)
        return profile.interests.all()


class CertificatesAPIView(generics.ListAPIView):
    serializer_class = CertificatesSerializer

    def get_queryset(self):
        profile_id = self.request.data['profile_id']
        profile = Profile.objects.get(pk=profile_id)
        return profile.certificates.all()


class FooterInfoAPIView(generics.RetrieveAPIView):
    serializer_class = FooterSerializer

    def get_object(self):
        profile_id = self.request.data['profile_id']
        profile = Profile.objects.select_related('contact_details') \
            .get(pk=profile_id)
        return profile.contact_details
