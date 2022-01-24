from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import QuestionnaireSerializer, ApplicationSerializer
from .models import Questionnaire, Application
from rest_framework import mixins


class QuestionnairePartnerViewSet(mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.CreateModelMixin,
                                  GenericViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    search_fields = ['last_name', 'first_name', 'patronymic']
    ordering_fields = ['last_name', 'date_created']


class ApplicationPartnerViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationOrganizationViewSet(mixins.ListModelMixin,
                                     mixins.RetrieveModelMixin,
                                     GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
