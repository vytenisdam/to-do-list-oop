from tasks import Task
from file_read import FileReader
from datetime import date
from datetime import datetime


class TaskList:
    def __init__(self):
        self.tasks = FileReader.file_read()

    def add_task(self, name, description, due_date, priority):
        new_task = Task(name,description,due_date, priority)
        name = new_task.get_task_name()
        description = new_task.get_task_description()
        # A way to access an attribute without a getter. Kazin ar iseina setint taip lengvai kaip accessing atributus be getteriu        
        priority = new_task.priority
        due_date = new_task.due_date
        creation_date = new_task.creation_date
        status = 'To be done.'
        self.tasks.append({'Task name': name , 'Description': description, 'Due date': due_date,'Priority': priority, 'Status': status, 'Creation date': creation_date})
        FileReader.write_file(self.tasks)
    
    def search_task_by_name(self, name):
        for task in self.tasks:
            if task['Task name'] == name:
                return task
                
    def remove_task(self,name):
        task_to_remove = self.search_task_by_name(name)
        self.tasks.remove(task_to_remove)
        FileReader.write_file(self.tasks)
    
    def edit_task(self,name,description,due_date):
        #editinimas bus removinant sena ir pridedant nauja vietoj jos
        pass
    
    def display_all_tasks(self):
        data = self.task_set_importance()
        for i in data:
            print(i)
    
    def sort_by_importance(self):
        self.tasks.sort(key=lambda x:x['Priority'],reverse=True)
        return self.tasks
        
    def sort_tasks_by_creation_date(self):
        self.tasks.sort(key=lambda x:x['Creation date'])
        return self.tasks
    
    def sort_tasks_by_due_date(self):
        self.tasks.sort(key=lambda x: datetime.strptime(x['Due date'], '%Y-%m-%d'))
        return self.tasks
        
    
    def mark_task_done(self,name):
        task_to_mark = self.search_task_by_name(name)
        task_to_mark['Status'] = f'Done on {str(date.today())}.'
        FileReader.write_file(self.tasks)
        
    def task_set_importance(self):
        tasks = []
        for task in self.tasks:
            if int(task['Priority']) >= 3:
                task['Priority'] = 'Very important'
                tasks.append(task)
            elif int(task['Priority']) <= 1:
                task['Priority'] = 'Not important'
                tasks.append(task)
            else:
                task['Priority'] = 'Average importance'
                tasks.append(task)
        return tasks
    
    def show_undone_tasks(self):
        data = self.task_set_importance()
        for i in data:
            if i['Status'] == 'To be done.':
                print(i)
        