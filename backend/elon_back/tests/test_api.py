import pytest
from django.urls import reverse

from mainapp.models import Advantage, MenuItem


@pytest.mark.django_db
def test_get_menu_items(api_client):
    # fit
    MenuItem.objects.create(title="Menu Item 1", order=4)
    # fit
    MenuItem.objects.create(title="Menu Item 2", order=2)
    # doesnt fit
    MenuItem.objects.create(title="Menu Item 3", order=3, is_displayed=False)
    # fit
    MenuItem.objects.create(title="Menu Item 4", order=1)

    url = reverse("menuitem-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert [item["title"] for item in response.data] == [
        "Menu Item 4",
        "Menu Item 2",
        "Menu Item 1",
    ]


@pytest.mark.django_db
def test_get_advantages(api_client):
    # fit
    Advantage.objects.create(
        title="Advantage 1", value="Value 1", description="Description 1", order=4
    )
    # fit
    Advantage.objects.create(
        title="Advantage 2", value="Value 2", description="Description 2", order=3
    )
    # doesnt fit
    Advantage.objects.create(
        title="Advantage 3",
        value="Value 3",
        description="Description 3",
        is_displayed=False,
        order=1,
    )

    url = reverse("advantages-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2
