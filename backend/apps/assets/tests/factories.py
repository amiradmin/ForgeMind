import factory

from apps.assets.models import Area, Asset, Organization, Plant


class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Sequence(lambda n: f"Organization {n}")

    code = factory.Sequence(lambda n: f"ORG-{n}")

    description = factory.Faker("text")

    website = factory.Faker("url")

    email = factory.Faker("email")

    phone = factory.Faker("phone_number")


class PlantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Plant

    name = factory.Sequence(lambda n: f"Plant {n}")

    code = factory.Sequence(lambda n: f"PL-{n}")

    organization = factory.SubFactory(OrganizationFactory)


class AreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Area

    name = factory.Sequence(lambda n: f"Area {n}")

    code = factory.Sequence(lambda n: f"AR-{n}")

    plant = factory.SubFactory(PlantFactory)


class AssetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Asset

    name = factory.Sequence(lambda n: f"Asset {n}")

    code = factory.Sequence(lambda n: f"AS-{n}")

    area = factory.SubFactory(AreaFactory)
