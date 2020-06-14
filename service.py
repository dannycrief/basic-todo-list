from collections import namedtuple
from datetime import datetime
from uuid import uuid4

Task = namedtuple('Task', ['date', 'text'])

TASKS = {}


def get_task(_id):
    if _id in TASKS:
        return TASKS[_id]


def get_all_tasks():
    return TASKS


def create_task(date, text):
    date_format = datetime.strptime(date, '%Y-%m-%d %H:%M')
    if date_format > datetime.now():
        task_id = str(uuid4())
        TASKS[task_id] = Task(date=date_format, text=text)
        return task_id


def update_task_by_id(task_id, text):
    if not task_id in TASKS:
        return
    TASKS[task_id] = text
