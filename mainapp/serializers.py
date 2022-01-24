from rest_framework.serializers import ModelSerializer
from .models import Questionnaire, Application, Organization, Offer


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OfferSerializer(ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Offer
        fields = '__all__'


class QuestionnaireSerializer(ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class ApplicationSerializer(ModelSerializer):
    customer_profile = QuestionnaireSerializer()
    # offer = OfferSerializer()

    class Meta:
        model = Application
        fields = '__all__'
