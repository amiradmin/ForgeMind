import pytest

from apps.assets.models import Asset
from apps.assets.tests.factories import (
    AreaFactory,
    AssetTypeFactory,
    OrganizationFactory,
    PlantFactory,
)
from apps.audit.models import AuditLog
from apps.audit.services import AuditService
from apps.identity.models import User


@pytest.mark.django_db
def test_audit_log_creation():

    user = User.objects.create_user(
        email="audit@test.com",
        password="password123",
    )

    organization = OrganizationFactory()

    plant = PlantFactory(
        organization=organization,
    )

    area = AreaFactory(
        plant=plant,
    )

    asset_type = AssetTypeFactory()

    asset = Asset.objects.create(
        area=area,
        asset_type=asset_type,
        name="Test Pump",
        code="TEST-PUMP-001",
    )

    audit = AuditService.log(
        user=user,
        action=AuditLog.Action.CREATE,
        instance=asset,
    )

    assert audit is not None

    assert AuditLog.objects.count() == 1
