from rest_framework import serializers

from personal_info.models import Profile, Interest, ContactDetails, Certificate


class MainInfoSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'middle_name', 'department_name']


class ContactDetailsSerializer(serializers.Serializer):
    country = serializers.CharField(
        max_length=60, source='office.address.country')
    region = serializers.CharField(
        max_length=60, source='office.address.region')
    locality = serializers.CharField(
        max_length=70, source='office.address.locality')
    street_name = serializers.CharField(
        max_length=130, source='office.address.street_name')
    street_number = serializers.IntegerField(
        source='office.address.street_number')
    apartment_number = serializers.IntegerField(
        source='office.address.apartment_number')
    postcode = serializers.IntegerField(
        source='office.postcode')
    telephone_extension = serializers.IntegerField(
        source='contact_details.telephone_extension')
    work_phone_number = serializers.CharField(
        max_length=17, source='contact_details.work_phone_number')
    additional_phone_number = serializers.CharField(
        max_length=17, source='contact_details.additional_phone_number')
    link_to_photo = serializers.CharField(
        max_length=100)
    telegram_name = serializers.CharField(
        max_length=35, source='contact_details.telegram_name')
    link_to_telegram = serializers.CharField(
        max_length=100, source='contact_details.link_to_telegram')
    link_to_vk = serializers.CharField(
        max_length=100, source='contact_details.link_to_vk')


class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('name', 'link_to_picture')


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('link_to_picture',)


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ('link_to_youtube', 'email', 'link_to_vk')
