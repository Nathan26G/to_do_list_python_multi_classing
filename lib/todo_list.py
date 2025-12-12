class TodoList():
    def __init__(self):
        self.todo_list = []
    
    def add(self, todo):
        self.todo_list.append(todo)
    
    def incomplete(self):
        incomplete_list = []
        for task in self.todo_list:
            if task['completion'] == False:
                incomplete_list.append(task)
        return incomplete_list
    
    def complete(self):
        complete_list = []
        for task in self.todo_list:
            if task['completion'] == True:
                complete_list.append(task)
        return complete_list
      
    def give_up(self):
        for task in self.todo_list:
            task['completion'] = True