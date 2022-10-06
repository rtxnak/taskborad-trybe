import pytest

from django.urls import reverse
from taskboard.models import Board, Task


@pytest.mark.django_db
def test_homepage(client):
    url = reverse('homepage')

    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_task(client):
    board = Board.objects.create(title="This is a board title")

    task = Task.objects.create(
        title="Task title",
        description="Task description",
        status="Pending",
        board_id=board
    )

    url = reverse('edittask')
    client.post(url, {'id': task.id, 'status': 'Doing'})

    task_from_db = Task.objects.first()

    assert task_from_db.status == 'Doing'