from shared.permissions.rbac import HasRBACPermission


class ViewPermission(HasRBACPermission):
    permission_code = ".view"


class CreatePermission(HasRBACPermission):
    permission_code = ".create"


class UpdatePermission(HasRBACPermission):
    permission_code = ".update"


class DeletePermission(HasRBACPermission):
    permission_code = ".delete"
