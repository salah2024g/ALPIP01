from enum import Enum


class Permission(str, Enum):

    READ = "read"
    WRITE = "write"
    ADMIN = "admin"



def has_permission(
    user_permissions: list,
    required: Permission
) -> bool:

    return required.value in user_permissions
