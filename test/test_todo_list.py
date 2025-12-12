from lib.todo_list import *
from unittest.mock import Mock


def test_empty_list_returned_when_TodoList_first_initialised():
    todo = TodoList()
    assert todo.todo_list  == []
    
def test_when_add_is_ran_task_with_completion_being_false_is_added_to_list():
    todo = TodoList()
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': False}
    todo.add(todo_task.task_dict)
    assert todo.todo_list  == [{'task': 'task', 'completion': False}]
    

def test_when_add_is_ran_task_with_completion_being_True_is_added_to_list():
    todo = TodoList()
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': True}
    todo.add(todo_task.task_dict)
    assert todo.todo_list  == [{'task': 'task', 'completion': True}]
    

def test_when_add_is_ran_multiple_times_multiple_tasks_are_added_to_list():
    todo = TodoList()
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': False}
    todo.add(todo_task.task_dict)
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': True}
    todo.add(todo_task.task_dict)
    assert todo.todo_list  == [{'task': 'task', 'completion': False}, {'task': 'task', 'completion': True}]


def test_incomplete_when_there_is_incomplete_task():
    todo = TodoList()
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': False}
    todo.add(todo_task.task_dict)
    assert todo.incomplete()  == [{'task': 'task', 'completion': False}]
    
def test_incomplete_when_there_is_not_incomplete_task():
    todo = TodoList()
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': True}
    todo.add(todo_task.task_dict)
    assert todo.incomplete()  == []
    
def test_complete_when_there_is_complete_task():
    todo = TodoList()
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': True}
    todo.add(todo_task.task_dict)
    assert todo.complete()  == [{'task': 'task', 'completion': True}]
    
def test_complete_when_there_is_not_complete_task():
    todo = TodoList()
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': False}
    todo.add(todo_task.task_dict)
    assert todo.complete()  == []
    

def test_length_of_complete_list_is_the_same_as_todo_list_after_give_up():
    todo = TodoList()
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': False}
    todo.add(todo_task.task_dict)
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': True}
    todo.add(todo_task.task_dict)
    todo_task = Mock('task')
    todo_task.task_dict = {'task': 'task', 'completion': False}
    todo.add(todo_task.task_dict)
    todo.give_up()
    len(todo.complete()) == len(todo.todo_list)