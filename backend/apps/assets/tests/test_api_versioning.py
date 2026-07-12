import pytest


@pytest.mark.django_db
def test_api_v1_assets_endpoint(client):

    url = "/api/v1/assets/"

    response = client.get(url)

    assert response.status_code in [
        401,
        200,
    ]
