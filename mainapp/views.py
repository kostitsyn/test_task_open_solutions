from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import QuestionnaireSerializer, ApplicationSerializer
from .models import Questionnaire, Application
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import generics
from .permissions import SuperUserOnly, PartnerOnly, OrganizationOnly


# class QuestionnaireListApiView(generics.ListAPIView):
#     renderer_classes = [JSONRenderer]
#     permission_classes = [SuperUserOnly, PartnerOnly]
#     queryset = Questionnaire.objects.all()
#     serializer_class = QuestionnaireSerializer
#
#
# class QuestionnaireRetrieveApiView(generics.RetrieveAPIView):
#     renderer_classes = [JSONRenderer]
#     permission_classes = [SuperUserOnly, PartnerOnly]
#     queryset = Questionnaire.objects.all()
#     serializer_class = QuestionnaireSerializer
#
#
# class QuestionnaireCreateAPIView(generics.CreateAPIView):
#     renderer_classes = [JSONRenderer]
#     permission_classes = [SuperUserOnly, PartnerOnly]
#     queryset = Questionnaire.objects.all()
#     serializer_class = QuestionnaireSerializer


class QuestionnairePartnerViewSet(ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    search_fields = ['first_name', 'last_name', 'patronymic']
    ordering_fields = ['last_name', 'date_created', 'date_updated']
    permission_classes = [SuperUserOnly, PartnerOnly]


class ApplicationPartnerViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [SuperUserOnly, PartnerOnly]


class ApplicationOrganizationViewSet(ModelViewSet):
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

