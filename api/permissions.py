from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, BasePermission
from rest_action_permissions.permissions import ActionPermission


class ProductPermission(ActionPermission):
    # The admin user can do anything
    enough_perms = IsAdminUser

    # Permissions for each action
    create_perms = IsAdminUser
    retrieve_perms = AllowAny
    update_perms = IsAdminUser
    partial_update_perms = IsAdminUser
    list_perms = AllowAny
    destroy_perms = IsAdminUser
    delete_perms = IsAdminUser

    # General permissions
    read_perms = AllowAny
    write_perms = IsAdminUser


class CategoryPermission(ActionPermission):
    # The admin user can do anything
    enough_perms = IsAdminUser

    # Permissions for each action
    create_perms = IsAdminUser
    retrieve_perms = AllowAny
    update_perms = IsAdminUser
    partial_update_perms = IsAdminUser
    list_perms = AllowAny
    destroy_perms = IsAdminUser
    delete_perms = IsAdminUser

    # General permissions
    read_perms = AllowAny
    write_perms = IsAdminUser


class BrandPermission(ActionPermission):
    # The admin user can do anything
    enough_perms = IsAdminUser

    # Permissions for each action
    create_perms = IsAdminUser
    retrieve_perms = AllowAny
    update_perms = IsAdminUser
    partial_update_perms = IsAdminUser
    list_perms = AllowAny
    destroy_perms = IsAdminUser
    delete_perms = IsAdminUser

    # General permissions
    read_perms = AllowAny
    write_perms = IsAdminUser