from django.contrib import admin
from .models import Offer, Application, Organization, Questionnaire
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from datetime import datetime


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'last_name', 'first_name', 'patronymic',
                    'phone', 'passport', 'get_offer_count', 'get_app_count')
    list_display_links = ('id', 'last_name', 'first_name', 'patronymic')
    search_fields = ('first_name', 'last_name', 'patronymic')
    list_filter = (('date_created', DateRangeFilter),)

    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

    def get_offer_count(self, object):
        return len(object.get_suitable_offers())

    get_offer_count.short_description = 'Подобранных предложений'

    def get_app_count(self, object):
        return len(object.quest_applications.all())
    get_app_count.short_description = 'Отправленных заявок'


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'get_last_name', 'get_first_name',
                    'get_patronymic', 'status', 'get_mobile', 'get_passport',
                    'get_partner')
    list_display_links = ('id', 'get_last_name', 'get_first_name', 'get_patronymic')
    list_filter = (('date_created', DateRangeFilter),)

    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

    def get_search_fields(self, request):
        return ['customer_profile__first_name', 'customer_profile__last_name',
                'customer_profile__patronymic']

    def get_last_name(self, object):
        return object.customer_profile.last_name
    get_last_name.short_description = 'Фамилия'

    def get_first_name(self, object):
        return object.customer_profile.first_name
    get_first_name.short_description = 'Имя'

    def get_patronymic(self, object):
        return object.customer_profile.patronymic
    get_patronymic.short_description = 'Отчество'

    def get_mobile(self, object):
        return object.customer_profile.phone
    get_mobile.short_description = 'Телефон'

    def get_passport(self, object):
        return object.customer_profile.passport
    get_passport.short_description = 'Пасспорт'

    def get_partner(self, object):
        return object.offer.organization.name
    get_partner.short_description = 'Партнер'



admin.site.register(Offer)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Organization)
admin.site.register(Questionnaire, QuestionnaireAdmin)

admin.site.site_title = 'Админ панель'
admin.site.site_header = 'Выберите заявку'
