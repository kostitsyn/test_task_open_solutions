from rest_framework.permissions import BasePermission


class SuperUserOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create']:
            return request.user.is_superuser


class PartnerOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_partner


class OrganizationOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_organization