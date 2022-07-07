from task2_1 import execute_task as task1
from task2_2 import execute_task as task2
from task2_3 import execute_task as task3
from task2_4 import execute_task as task4
from task2_5 import execute_task as task5
from task2_6 import execute_task as task6
from task2_7 import execute_task as task7
from task2_8 import execute_task as task8

is_exit_request = False
available_tasks = {
    "2.1": task1,
    "2.2": task2,
    "2.3": task3,
    "2.4": task4,
    "2.5": task5,
    "2.6": task6,
    "2.7": task7,
    "2.8": task8
}

while not is_exit_request:
    print("Select task")
    for task in available_tasks: print("\t* {}".format(task))
    print("or enter q for exit\n")

    task = input()
    if task == "q":
        is_exit_request = True
        continue
    elif task not in available_tasks:
        print("\nWrong choice, please enter something different\n")
    else:
        available_tasks[task]();