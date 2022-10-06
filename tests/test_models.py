import pytest
from taskboard.models import Board, Task
from django.forms import ValidationError


@pytest.fixture
def board():
    return Board(title="this is a board title")


@pytest.mark.django_db
def test_board_model(board):
    board.save()

    boards_from_db = Board.objects.all()

    assert len(boards_from_db) == 1
    assert boards_from_db[0].title == "this is a board title"


@pytest.fixture
def task():
    return Task(
      title="task title",
      description="task description",
      status="Pending"
      )


@pytest.mark.django_db
def test_task_model(board, task):
    board.save()

    task.board_id = board
    task.save()

    assert Task.objects.count() == 1

    task_from_db = Task.objects.filter(board_id=board).first()

    assert (
        task_from_db.title,
        task_from_db.description,
        task_from_db.status,
    ) == (
        "task title",
        "task description",
        "Pending",
      )


@pytest.mark.django_db
def test_task_model_invalid_statusS(board, task):
    board.save()

    task.board_id = board
    task.status = "INVALID STATUS"

    with pytest.raises(ValidationError):
        task.full_clean()
