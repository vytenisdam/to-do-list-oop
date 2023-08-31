from task__list import TaskList
from tasks import Task
from file_read import FileReader


#Kazkaip padaryt kad inputint reiktu metus menesi ir dieena atskirai ir po to juos sujungt per '-' ir turet string.
#Pridet task priority(1-3, not important - important)/padaryt per if, kad ivest galetum skaiciu bet rodytu assigned reiksme 1 - not important, 2 - average importance, 3 - very important
#Status - (done/to be done/)
#Kaip padaryt kadd nereiktu ivest tikslaus pavadinimo uztektu tik zodzio ir grazintu visas susijusias tasks kaip display
#darant prompta displayinant taskus kiekviena kart reikia is naujo nuskaityt self.tasks, kad nepakliutu priority reiksmes kaip str, visad turi but int kad veiktu funkcijose


list_of_tasks = TaskList()
print("welcome to your To do list. Here's all your tasks:")
is_on = True
while is_on == True:
    choice = input('What would you like to do add/remove/edit task or see tasks list sorted by importance/creation/due dates or task done?')
    if choice == 'add':
        pass
    elif choice == 'remove':
        pass
    elif choice == 'edit':
        pass
    elif choice == 'done':
        pass
    elif choice == 'due date':
        pass
    elif choice == 'creation date':
        pass
    elif choice == 'importance':
        pass
    
        
#list_of_tasks.add_task('kwtc','sasda','2023-12-15', 6)
#list_of_tasks.mark_task_done('pirma')
#list_of_tasks.add_task('antra','betkas','2023-10-19',1)
#list_of_tasks.display_all_tasks()
# print(list_of_tasks.sort_tasks_by_creation_date())
#list_of_tasks.sort_by_importance()

#list_of_tasks.show_undone_tasks()
