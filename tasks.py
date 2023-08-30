from datetime import date

class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        # if priority == 3:
        #     self.priority = 'Very important'
        # elif priority == 1:
        #     self.priority = 'Low importance'
        # else:
        #     self.priority = 'Average importance'
        self.status = 'To be done.'
        self.creation_date = date.today()

    def get_task_name(self):
        return self.name
    
    def get_task_due_date(self):
        return self.due_date
    
    def get_task_creation_date(self):
        return self.creation_date
    
    def get_task_description(self):
        return self.description
    
    def set_task_name(self,new_name):
        self.name = new_name

    def set_task_description(self, new_desc):
        self.description = new_desc
        
    def set_task_due_date(self,new_due_date):
        self.due_date = new_due_date
