class Todo():
    def __init__(self, task):
        self.task_dict = {'task': str(task), 'completion': False}
    
    def mark_complete(self):
        self.task_dict['completion'] = True