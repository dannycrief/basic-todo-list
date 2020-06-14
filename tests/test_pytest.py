import datetime
from mock import MagicMock

from app import get_parameters_for_task_creation, format_date

import pytest

import service

TASK_ID = 1
TASK_TEXT = "text text"
TASKS = {TASK_ID: TASK_TEXT}


def test_get_task_id_exists(tasks):
    result_task = service.get_task(TASK_ID)
    assert result_task == TASK_TEXT


def test_get_task_doesnt_exist(tasks):
    result_task = service.get_task(2)
    assert result_task is None


def test_get_all_tasks_empty(tasks_empty):
    service.TASKS = {}
    all_tasks = service.get_all_tasks()
    assert all_tasks == {}
    service.TASKS = TASKS


def test_get_all_tasks_not_empty(tasks):
    all_tasks = service.get_all_tasks()
    assert all_tasks == TASKS


def test_create_task_success():
    date = (
            datetime.datetime.now() +
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    task = service.create_task(date, TASK_TEXT)
    assert task


def test_create_task_in_the_past():
    date = (
            datetime.datetime.now() -
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")

    task = service.create_task(date, TASK_TEXT)
    assert task is None


def test_get_parameters_ok():
    args = MagicMock(date="date", text="text")
    text, date = get_parameters_for_task_creation(args)
    assert text == text
    assert date == date


def test_get_parameters_invalid():
    args = MagicMock()
    args.get.side_effect = ['text', None]
    text, date = get_parameters_for_task_creation(args)
    assert date is None
    assert text == text


def test_format_date_valid():
    date = '2102-01-01 12:12'
    res = format_date(date)
    assert res == datetime.datetime(2102, 1, 1, 12, 12)


@pytest.mark.parametrize('invalid_date', ['2012-01-01 12:12', '2102-01-01'])
def test_format_date_invalid(invalid_date):
    res = format_date(invalid_date)
    assert res is None
