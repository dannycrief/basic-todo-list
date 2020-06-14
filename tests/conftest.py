import pytest

import service

TASK_ID = 1
TASK_TEXT = "text text"
TASKS = {TASK_ID: TASK_TEXT}


@pytest.fixture()
def tasks():
    service.TASKS = TASKS


@pytest.fixture()
def tasks_empty():
    service.TASKS = TASKS
