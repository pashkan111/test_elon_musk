import pytest
from django.urls import reverse

from mainapp.models import Advantage, MenuItem


@pytest.mark.django_db
def test_get_menu_items(api_client):
    # fit
    MenuItem.objects.create(name="Menu Item 1", order=1)
    # fit
    MenuItem.objects.create(name="Menu Item 2", order=2)
    # doesnt fit
    MenuItem.objects.create(name="Menu Item 3", order=3, is_displayed=False)

    url = reverse("menuitem-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_get_advantages(api_client):
    # fit
    Advantage.objects.create(
        title="Advantage 1",
        value="Value 1",
        description="Description 1",
    )
    # fit
    Advantage.objects.create(
        title="Advantage 2",
        value="Value 2",
        description="Description 2",
    )
    # doesnt fit
    Advantage.objects.create(
        title="Advantage 3",
        value="Value 3",
        description="Description 3",
        is_displayed=False,
    )

    url = reverse("advantages-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2
