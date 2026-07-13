from apps.identity.permissions.rbac import HasPermission


class CanViewAsset(HasPermission):
    permission_code = "asset.view"


class CanCreateAsset(HasPermission):
    permission_code = "asset.create"


class CanUpdateAsset(HasPermission):
    permission_code = "asset.update"


class CanDeleteAsset(HasPermission):
    permission_code = "asset.delete"
