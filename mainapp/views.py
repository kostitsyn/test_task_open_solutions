from rest_framework.viewsets import ModelViewSet
from .serializers import QuestionnaireSerializer, ApplicationSerializer
from .models import Questionnaire, Application


class QuestionnaireModelViewSet(ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    search_fields = ['last_name', 'first_name', 'patronymic']
    ordering_fields = ['last_name', 'date_created']


class ApplicationModelViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


