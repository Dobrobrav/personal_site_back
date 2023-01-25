from django.db import models


class Address(models.Model):
    country = models.CharField(
        max_length=60, verbose_name='Страна',
    )
    region = models.CharField(
        max_length=60, blank=True, null=True,
        verbose_name='Регион (область)',
    )
    locality = models.CharField(
        max_length=70, verbose_name='Населенный пункт',
    )
    street_name = models.CharField(
        max_length=130, verbose_name='Улица',
    )
    street_number = models.IntegerField(
        verbose_name='Дом',
    )
    apartment_number = models.IntegerField(
        blank=True, null=True,
        verbose_name='Номер',
    )
    postcode = models.IntegerField(
        verbose_name='Почтовый индекс',
    )

    def __str__(self):
        return f"ул. {self.street_name}, дом. {self.street_number}, " \
               f"номер. {self.apartment_number}"

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class ContactDetails(models.Model):
    email = models.EmailField(
        blank=True, null=True,
        verbose_name='Почта',
    )
    telephone_extension = models.CharField(
        max_length=10, blank=True, null=True,
        verbose_name='Внутренний телефон',
    )
    work_phone_number = models.CharField(
        max_length=17, blank=True, null=True,
        verbose_name='Рабочий телефон',
    )
    additional_phone_number = models.CharField(
        max_length=17, blank=True, null=True,
        verbose_name='Дополнительный телефон',
    )
    telegram_name = models.CharField(
        max_length=35, blank=True, null=True,
        verbose_name='Название телеграм-аккаунта',
    )
    link_to_telegram = models.URLField(
        blank=True, null=True,
        verbose_name='Ссылка на телеграм-аккаунт',
    )
    link_to_vk = models.URLField(
        blank=True, null=True,
        verbose_name='Ссылка на ВК-аккаунт',
    )
    link_to_youtube = models.URLField(
        blank=True, null=True,
        verbose_name='Ссылка на ютуб-канал',
    )

    def __str__(self):
        return str(self.work_phone_number)

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'


class Department(models.Model):
    name = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name='Название',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Office(models.Model):
    address = models.ForeignKey(
        Address, on_delete=models.DO_NOTHING,
        verbose_name='Адрес',
    )

    def __str__(self):
        return f"офис по адресу {self.address}"

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30, verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=30, verbose_name='Фамилия',
    )
    middle_name = models.CharField(
        max_length=30, blank=True, null=True,
        verbose_name='Отчество'
    )
    department = models.ForeignKey(
        Department, models.DO_NOTHING,
        verbose_name='Отдел',
    )
    office = models.ForeignKey(
        Office, models.DO_NOTHING, blank=True, null=True,
        verbose_name='Офис', )
    contact_details = models.ForeignKey(
        ContactDetails, models.DO_NOTHING,
        verbose_name='Контактные данные',
    )
    link_to_photo = models.URLField(
        blank=True, null=True,
        verbose_name='Ссылка на фото',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Interest(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Название',
    )
    link_to_picture = models.URLField(
        blank=True, null=True,
        verbose_name='Ссылка на картинку',
    )
    profiles = models.ManyToManyField(
        Profile, related_name='interests',
        verbose_name='Профили',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Интерес'
        verbose_name_plural = 'Интересы'
        ordering = ['id']


class Certificate(models.Model):
    # name = models.CharField(max_length=150)
    link_to_picture = models.URLField(
        blank=True, null=True,
        verbose_name='Ссылка на картинку',
    )
    profiles = models.ManyToManyField(
        Profile, related_name='certificates',
        verbose_name='Профили',
    )

    def __str__(self):
        return f"certificate: {self.pk}"

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        ordering = ['id']
