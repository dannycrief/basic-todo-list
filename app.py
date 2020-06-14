from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

from service import get_task, get_all_tasks, create_task, update_task_by_id


class APIException(Exception):
    status_code = 404

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/tasks", methods=['GET'])
def tasks_list():
    tasks = get_all_tasks()
    return jsonify(tasks=tasks)


@app.route("/tasks/<int:task_id>", methods=['GET'])
def task_by_id(task_id):
    task = get_task(task_id)
    if not task:
        raise APIException("Task doesn't exist")
    return jsonify(task=task)


@app.route("/tasks/<int:task_id>", methods=['PUT'])
def task_update_by_id(task_id):
    text = request.args.get('text')
    update_task_by_id(task_id, text)
    if not task_id:
        raise APIException("Task doesn't exist")

    return jsonify({'task_id': task_id})


from uuid import uuid4
from collections import namedtuple

TASKS = {}
Task = namedtuple('Task', ['date', 'text'])


def get_parameters_for_task_creation(args):
    text = args.get('text')
    date = args.get('date')
    return text, date


def format_date(date):
    try:
        date_format = datetime.strptime(date, '%Y-%m-%d %H:%M')
        if date_format > datetime.now():
            return date_format
    except ValueError:
        return None


@app.route("/tasks", methods=['POST'])
def task_post():
    text, date = get_parameters_for_task_creation(request.args)
    if not (text and date):
        APIException(status_code=412, message='Text and date should not be empty')

    date_format = format_date(date)
    if not date_format:
        raise APIException(
            status_code=412, message='Date should be in the future in format %Y-%m-%d %H:%M')
    task_id = str(uuid4())
    TASKS[task_id] = Task(date=date_format, text=text)

    if task_id:
        return jsonify({'task_id': task_id})
    raise APIException(status_code=412, message='Date should be in the future')


if __name__ == '__main__':
    app.run()
