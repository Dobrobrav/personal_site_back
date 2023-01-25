from django.apps import AppConfig


class PersonalInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal_info'
    verbose_name = 'Личная информация'
