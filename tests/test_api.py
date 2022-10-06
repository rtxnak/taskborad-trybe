from rest_framework.test import APIClient
import pytest
from django.urls import reverse
from taskboard.models import Board


@pytest.fixture
def api_client():
    return APIClient()
  

@pytest.mark.django_db
def test_list_boards(api_client):
    N_BOARDS = 3

    for i in range(N_BOARDS):
        Board.objects.create(title=f"Board {i}")

    url = reverse('board-list')
    response = api_client.get(url)

    assert response.status_code == 200

    data = response.json()
    assert len(data) == N_BOARDS

    for i, board in enumerate(data):
        assert board['title'] == f"Board {i}"


@pytest.mark.django_db
def test_create_board(api_client):
    url = reverse('board-list')
    response = api_client.post(url, {'title': 'My board title'}, format='json')

    assert response.status_code == 201

    assert Board.objects.count() == 1

    board_from_db = Board.objects.first()
    assert board_from_db.title == 'My board title'
    