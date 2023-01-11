from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, BasePermission
from rest_action_permissions.permissions import ActionPermission


# Is the user a Product Manager?
class IsProductManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Product Manager').exists()


# Is the user an Account Manager?
class IsAccountManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Account Manager').exists()


class IsAPIManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='API Manager').exists()


class ProductPermission(ActionPermission):
    # The admin user can do anything
    enough_perms = IsAdminUser

    # General permissions
    read_perms = AllowAny
    write_perms = IsAPIManager


class CategoryPermission(ActionPermission):
    # The admin user can do anything
    enough_perms = IsAdminUser

    # General permissions
    read_perms = AllowAny
    write_perms = IsAPIManager


class BrandPermission(ActionPermission):
    # The admin user can do anything
    enough_perms = IsAdminUser

    # General permissions
    read_perms = AllowAny
    write_perms = IsAPIManager
