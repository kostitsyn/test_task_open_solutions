from django.contrib import admin
from .models import Offer, Application, Organization, Questionnaire


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'last_name', 'first_name', 'patronymic')

admin.site.register(Offer)
admin.site.register(Application)
admin.site.register(Organization)
admin.site.register(Questionnaire, QuestionnaireAdmin)

admin.site.site_title = 'Админ панель'
admin.site.site_header = 'Выберите заявку'
