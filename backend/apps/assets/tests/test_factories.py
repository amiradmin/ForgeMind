from apps.assets.tests.factories import AreaFactory, AssetFactory, OrganizationFactory, PlantFactory


def test_factories_create_objects(db):
    organization = OrganizationFactory()
    plant = PlantFactory()
    area = AreaFactory()
    asset = AssetFactory()

    assert organization.id is not None
    assert plant.organization is not None
    assert area.plant is not None
    assert asset.area is not None
