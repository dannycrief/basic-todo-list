# basic_todo_list
[![Travis][build-badge]][build]


[build-badge]: https://img.shields.io/travis/tomasmor42/basic_todo_list/master.png?style=flat-square
[build]: https://travis-ci.org/tomasmor42/basic_todo_list

Basic Flask-Based to-do application. 
How to start:
* clone this repo;
* Go to the repo folder basic_todo_list;
* Create a virtual environment `python -m venv venv`;
* Activate it `source venv/bin/activate` (or `virtualenv venv`)
* Install the `requirements pip install -r requirements.txt`;
* Set PYTHONPATH with current directory: `export PYTHONPATH=current_folder`
* You can start an app with python app.py. It will start at `http://127.0.0.1:5000/`
* This application has following endpoint: 
  * GET: tasks: gives all stored tasks;
  * GET: /tasks/<int:task_id>: gives text of the task by id
  * POST: /tasks/post: create a task. Takes task date (suppose to be in the future) and text in request arguments. 
* To run tests you can run `pytest tests/test_pytest.py`



Это небольшое приложение на Flask, которое представляет собой простйший todo-лист. 
Как начать: 
* склонировать этот репозиторий;
* перейти в папку с ним; 
* создать виртуальное окружение `python -m venv venv`;
* активировать его `source venv/bin/activate` (или `virtualenv venv`)
* установить зависимости `requirements pip install -r requirements.txt`;
* переменную окружения сделать равно текущей директории (текущую директорию можно узнать выполнив команду `pwd`) PYTHONPATH: `export PYTHONPATH=current_folder` (или `set PYTHONPATH=current_folder`)
* Запустить приложение можно с помощью команды `python app.py`. Оно запустится по адресу `http://127.0.0.1:5000/`
* У этого приложения есть следующие эндпоинты: 
  * GET: tasks: возвращает все существующие задачи;
  * GET: /tasks/<int:task_id>: возвращает задачу с заданным id; 
  * POST: /tasks/post: создает задачу. Принимает дату задачи (которая должна быть в будущем) и текст в параметрах запроса. 
  * Запустить тесты можно с помощью команды `pytest tests/test_pytest.py`


