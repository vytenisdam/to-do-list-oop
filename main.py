from task__list import TaskList
from tasks import Task
from file_read import FileReader


#Kazkaip padaryt kad inputint reiktu metus menesi ir dieena atskirai ir po to juos sujungt per '-' ir turet string.
#Pridet task priority(1-3, not important - important)/padaryt per if, kad ivest galetum skaiciu bet rodytu assigned reiksme 1 - not important, 2 - average importance, 3 - very important
#Status - (done/to be done/)
#Kaip padaryt kadd nereiktu ivest tikslaus pavadinimo uztektu tik zodzio ir grazintu visas susijusias tasks kaip display


list_of_tasks = TaskList()
#list_of_tasks.add_task('kwtc','sasda','2023-12-15', 6)
#list_of_tasks.mark_task_done('pirma')
#list_of_tasks.add_task('antra','betkas','2023-10-19',1)
list_of_tasks.display_all_tasks()