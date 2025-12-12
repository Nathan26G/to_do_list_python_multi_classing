# Planned functions

## File: lib/todo_list.py
```python
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass
```

## File: lib/todo.py

```python
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass
```

# test planning 
## File: test/test_todo_list.py

```python

'''
empty list returned when TodoList first initialised
'''
todo = TodoList()
todo.todo_list # => []


'''
when add is ran, task with completion being false is added to list
'''
todo = TodoList()
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: False}
todo.add(todo_task.task_dict)
todo.todo_list # => [{task: task, completion: False}]

'''
when add is ran, task with completion being True is added to list
'''
todo = TodoList()
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: True}
todo.add(todo_task.task_dict)
todo.todo_list # => [{task: task, completion: True}]

'''
when add is ran multiple times, multiple tasks are added to list
'''
todo = TodoList()
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: False}
todo.add(todo_task.task_dict)
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: True}
todo.add(todo_task.task_dict)
todo.todo_list # => [{task: task, completion: False}, {task: task, completion: True}]


'''
test incomplete when there is incomplete task
'''
todo = TodoList()
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: False}
todo.add(todo_task.task_dict)
todo.incomplete # => [{task: task, completion: False}]

'''
test incomplete when there is not incomplete task
'''
todo = TodoList()
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: True}
todo.add(todo_task.task_dict)
todo.incomplete # => []

'''
test complete when there is complete task
'''
todo = TodoList()
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: True}
todo.add(todo_task.task_dict)
todo.incomplete # => [{task: task, completion: True}]

'''
test complete when there is not complete task
'''
todo = TodoList()
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: False}
todo.add(todo_task.task_dict)
todo.incomplete # => []


'''
test length of complete list is the same as todo list after give up
'''
todo = TodoList()
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: False}
todo.add(todo_task.task_dict)
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: True}
todo.add(todo_task.task_dict)
todo_task = Mock(task)
todo_task.task_dict = {task: task, completion: False}
todo.add(todo_task.task_dict)
todo.give_up()
len(todo.complete) == len(todo.todo_list)
```

## File: test/test_todo.py

```python

'''
task dict in correct format and has correct bool when initialised
'''
task = Todo(task)
task.task_dict # => {task: task, completion: False}

'''
completetion bool changes after mark_complete
'''
task = Todo(task)
task.mark_complete()
task.task_dict # => {task: task, completion: True}

```

## File: test/test_todo_list_integration.py

```python
'''
when add is ran, task with completion being false is added to list
'''
todo = TodoList()
todo_task = Todo(task)
todo.add(todo_task.task_dict)
todo.todo_list # => [{task: task, completion: False}]

'''
when add is ran, task with completion being True is added to list
'''
todo = TodoList()
todo_task = Todo(task)
todo_task.mark_complete()
todo.add(todo_task.task_dict)
todo.todo_list # => [{task: task, completion: True}]

'''
when add is ran multiple times, multiple tasks are added to list
'''
todo = TodoList()
todo_task = Todo(task)
todo.add(todo_task.task_dict)
todo_task = Todo(task)
todo_task.mark_complete()
todo.add(todo_task.task_dict)
todo.todo_list # => [{task: task, completion: False}, {task: task, completion: True}]


'''
test incomplete when there is incomplete task
'''
todo = TodoList()
todo_task = Todo(task)
todo.add(todo_task.task_dict)
todo.incomplete # => [{task: task, completion: False}]

'''
test incomplete when there is not incomplete task
'''
todo = TodoList()
todo_task = Todo(task)
todo_task.mark_complete()
todo.add(todo_task.task_dict)
todo.incomplete # => []

'''
test complete when there is complete task
'''
todo = TodoList()
todo_task = Todo(task)
todo_task.mark_complete()
todo.add(todo_task.task_dict)
todo.incomplete # => [{task: task, completion: True}]

'''
test complete when there is not complete task
'''
todo = TodoList()
todo_task = Todo(task)
todo.add(todo_task.task_dict)
todo.incomplete # => []


'''
test length of complete list is the same as todo list after give up
'''
todo = TodoList()
todo_task = Todo(task)
todo.add(todo_task.task_dict)
todo_task = Todo(task)
todo_task.mark_complete()
todo.add(todo_task.task_dict)
todo_task = Todo(task)
todo.add(todo_task.task_dict)
todo.give_up()
len(todo.complete) == len(todo.todo_list)
```