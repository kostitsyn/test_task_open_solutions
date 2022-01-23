from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Organization(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название огранизации')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return f'Организация {self.name}'


class Offer(models.Model):
    OFFER_TYPES = [
        ['CC', 'Потребительский кредит'],
        ['MG', 'Ипотека'],
        ['CL', 'Автокредит'],
        ['KM', 'КМСБ'],
    ]

    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата и время создания')
    date_updated = models.DateTimeField(auto_now=True,
                                        verbose_name='Дата и время изменения')
    date_start_rotation = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время начала ротации')
    date_end_rotation = models.DateTimeField(blank=True, null=True, verbose_name='Дата и время окончания ротации')
    offer_name = models.CharField(max_length=128, unique=True, verbose_name='Название предложения')
    offer_type = models.CharField(max_length=2, choices=OFFER_TYPES,
                                  verbose_name='Тип предложения')
    min_scoring = models.IntegerField(default=0, verbose_name='Минимальный скоринговый балл')
    max_scoring = models.IntegerField(default=0, verbose_name='Максимальный	скоринговый	балл')
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL,
                                     verbose_name='Кредитная организация',
                                     related_name='offers')

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return f'Предложение {self.offer_name}'


class Questionnaire(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    patronymic = models.CharField(max_length=128, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    passport = models.IntegerField(verbose_name='Номер паспорта', unique=True)
    scoring = models.IntegerField(default=0, verbose_name='Скоринговый балл')

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        return f'Анкета клиента {self.first_name} {self.last_name}'


class Application(models.Model):
    STATUS_TYPES = [
        ['N', 'NEW'],
        ['S', 'SENT']
    ]

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата и время отправки')
    customer_profile = models.ForeignKey(Questionnaire, on_delete=models.CASCADE,
                                         verbose_name='Анкета клиента',
                                         related_name='quest_applications')
    offer = models.ForeignKey(Offer, null=True, on_delete=models.SET_NULL, verbose_name='Предложение',
                              related_name='offer_applications')
    status = models.CharField(max_length=1, choices=STATUS_TYPES, verbose_name='Статус')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка №{self.id} от {self.customer_profile.first_name} {self.customer_profile.last_name}'


