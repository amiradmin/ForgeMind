import pytest

from apps.assets.tasks import process_asset_metadata
from apps.assets.tests.factories import AssetFactory


@pytest.mark.django_db
def test_process_asset_metadata_task():

    asset = AssetFactory()

    result = process_asset_metadata(
        str(asset.id),
    )

    assert result["status"] == "processed"

    assert result["asset_id"] == str(asset.id)