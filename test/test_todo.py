from lib.todo import *


def test_task_dict_in_correct_format_and_has_correct_bool_when_initialised():
    task = Todo('task')
    assert task.task_dict  == {'task': 'task', 'completion': False}
    

def test_completetion_bool_changes_after_mark_complete():
    task = Todo('task')
    task.mark_complete()
    assert task.task_dict  == {'task': 'task', 'completion': True}