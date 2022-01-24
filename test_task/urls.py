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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from mainapp.views import QuestionnairePartnerViewSet, ApplicationPartnerViewSet, ApplicationOrganizationViewSet
from rest_framework.authtoken import views


partner_router = DefaultRouter()
partner_router.register('questionnaires', QuestionnairePartnerViewSet, basename='questionnaires')
partner_router.register('create_application', ApplicationPartnerViewSet, basename='create_application')

organization_router = DefaultRouter()
organization_router.register('applications', ApplicationOrganizationViewSet, basename='applications')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/partners/', include(partner_router.urls)),
    path('api/organizations/', include(organization_router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('admin-tools/', include('admin_tools.urls'))
]
