from task__list import TaskList
from tasks import Task
from file_read import FileReader


#Kazkaip padaryt kad inputint reiktu metus menesi ir dieena atskirai ir po to juos sujungt per '-' ir turet string.
#Pridet task priority(1-3, not important - important)/padaryt per if, kad ivest galetum skaiciu bet rodytu assigned reiksme 1 - not important, 2 - average importance, 3 - very important
#Status - (done/to be done/)

list_of_tasks = TaskList()
# list_of_tasks.add_task('pirma','pirmassas','2023-09-15', 3)
#list_of_tasks.mark_task_done('pirma')
list_of_tasks.display_all_tasks()