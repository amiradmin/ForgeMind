from apps.identity.permissions.rbac import HasPermission


class CanViewMaintenancePlan(HasPermission):
    permission_code = "maintenance_plan.view"


class CanCreateMaintenancePlan(HasPermission):
    permission_code = "maintenance_plan.create"


class CanUpdateMaintenancePlan(HasPermission):
    permission_code = "maintenance_plan.update"


class CanDeleteMaintenancePlan(HasPermission):
    permission_code = "maintenance_plan.delete"


class CanViewMaintenanceRequest(HasPermission):
    permission_code = "maintenance_request.view"


class CanCreateMaintenanceRequest(HasPermission):
    permission_code = "maintenance_request.create"


class CanUpdateMaintenanceRequest(HasPermission):
    permission_code = "maintenance_request.update"


class CanDeleteMaintenanceRequest(HasPermission):
    permission_code = "maintenance_request.delete"


class CanViewWorkOrder(HasPermission):
    permission_code = "work_order.view"


class CanCreateWorkOrder(HasPermission):
    permission_code = "work_order.create"


class CanUpdateWorkOrder(HasPermission):
    permission_code = "work_order.update"


class CanDeleteWorkOrder(HasPermission):
    permission_code = "work_order.delete"
