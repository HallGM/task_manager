import pdb
from models.task import Task
import repositories.task_repository as task_repository  

task_1 = Task("Walk Dog", "Jack Jarvis", 60)

task_2 = Task("Feed Cat", "Victor McDade", 5)

print(task_1.__dict__)
pdb.set_trace()
task_repository.save(task_2)

res = task_repository.select_all() 

for task in res:
    print(task.__dict__)
