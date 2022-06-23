from task2_1 import execute_task as task1
from task2_2 import execute_task as task2
from task2_3 import execute_task as task3

is_exit_request = False
available_tasks = {
    "2.1": task1,
    "2.2": task2,
    "2.3": task3
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