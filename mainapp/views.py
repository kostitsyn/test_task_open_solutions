from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import QuestionnaireSerializer, ApplicationSerializer
from .models import Questionnaire, Application
from rest_framework import mixins
from rest_framework.response import Response


class QuestionnairePartnerViewSet(mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.CreateModelMixin,
                                  GenericViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    search_fields = ['first_name', 'last_name', 'patronymic']
    ordering_fields = ['last_name', 'date_created', 'date_updated']


class ApplicationPartnerViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationOrganizationViewSet(mixins.ListModelMixin,
                                     mixins.RetrieveModelMixin,
                                     GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    search_fields = [
        'customer_profile__first_name',
        'customer_profile__last_name',
        'customer_profile__patronymic'
    ]
    ordering_fields = [
        'customer_profile__first_name',
        'customer_profile__last_name',
        'date_created',
        'date_updated'
    ]

    def retrieve(self, request, pk=None):
        application = Application.objects.get(pk=pk)
        application.set_received()
        serializer = self.serializer_class(application)
        return Response(serializer.data)

