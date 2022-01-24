"""test_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_nested import routers
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainapp.views import QuestionnairePartnerViewSet, ApplicationPartnerViewSet, ApplicationOrganizationViewSet


router = DefaultRouter()

# router.register('partner_questionnaires', QuestionnairePartnerViewSet)
# router.register('partner_applications', ApplicationPartnerViewSet)

# router.register('organization_applications', ApplicationOrganizationViewSet)


# router.register('partner', router, basename='partner')
# router.register('organization', router, basename='organization')

partner_router = routers.NestedSimpleRouter(router, 'partners', lookup='partner')
partner_router.register('partner_questionnaires1', QuestionnairePartnerViewSet, basename='questionnaire_partner')
partner_router.register('partner_applications1', ApplicationPartnerViewSet, basename='organization_partner')

organization_router = routers.NestedSimpleRouter(router, 'organizations', lookup='organization')
organization_router.register('orga')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/partner/', include(partner_router.urls)),
    path('api/organization/', include(organization_router.urls))
]
