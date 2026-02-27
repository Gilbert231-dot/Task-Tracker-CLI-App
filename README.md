# How to use my Task Tracker CLI App

## Tack Tracker CLI App
A command-line interface application built with Python.

## Features
- Add task
- Update task
- check status or change status
- Delete task
- List all tasks created
- List all tasks with 'status': 'Done'
- List all tasks with 'status': 'In progress'
- List all tasks with 'status': 'todo'

### Installation
Clone this Repository
Navigate to the project folder(MyFirstProject)
Run `python main.py`

### Usage
python main.py add "Buy groceries"
python main.py update 1 "Go to bed"
python main.py status 1
python main.py delete 1
python main.py listing
python main.py done
python main.py inprogress
python main.py todo

### Storage
`task_container.json` file for storage
