from platform import system as sysName
from os import system
from time import sleep
from os import path

def clearScreen():
    # mac and linux
    if sysName() == "Linux" or sysName == "Darwin":
        system("clear")
    # windows
    elif sysName() == "Windows":
        system("cls")

def createFiles():
    if not path.isfile("tasks.txt"):
        with open("tasks.txt", 'w') as f:
            f.write('')
    if not path.isfile("done_tasks.txt"):
        with open("done_tasks.txt", 'w') as f:
            f.write('')

def showMenu():
    clearScreen()
    with open("tasks.txt") as f:
        tasks = f.readlines()
    print(
        "\n########################################################"
        "\n------------------------ TO DO -------------------------"
        "\n########################################################"
        "\n"
    )
    if not tasks:
        print("You're all done")
    i = 1
    
    for task in tasks:
        print(f"{i}. {task}", end='')
        i += 1
    print('\n')
    with open("done_tasks.txt") as f:
        done_tasks = f.readlines()
    if done_tasks:
        print(
            "########################################################\n"
            "---------------------- Done tasks ----------------------\n"
            "########################################################\n"
        )
    i = 1
    for task in done_tasks:
        print(f"{i}. {task}", end='')
        i += 1
    print()

def addTask(task):
    with open("tasks.txt", 'a') as f:
        f.write(f"{task}\n")

def removeTask(task):
    if type(task).__name__ != int.__name__:
        print("Wrong task!")
        sleep(2)
        return
    
    with open("tasks.txt") as f:
        tasks = f.readlines()

    if not tasks:
        print("There is no task!")
        sleep(2)
        return
    elif task > len(tasks):
        print("This task doesn't exist")
        sleep(2)
        return
    
    removed_task = tasks[task - 1]
    tasks = tasks[:task - 1] + tasks[task:]
    # print(tasks)
    with open("tasks.txt", 'w') as f:
        f.writelines(tasks)
    return removed_task

def doneTask(task):
    done_task = removeTask(task)
    if done_task:
        with open('done_tasks.txt', 'a') as f:
            f.write(f"{done_task}")

def showHelp():
    clearScreen()
    print(
        "\n########################################################"
        "\n#                       TO DO                          #"
        "\n########################################################"
        "\n#                        HELP                          #"
        "\n########################################################"
        "\n"
        "\n+: Enter + to add task. (+ task)"
        "\n-: Enter - to remove task. (- task_line)"
        "\n/: Enter / to mark task as complete. (/ task_line)"
        "\n0: Enter 0 to exit. (0)"
    )
    input("\nEnter something to continue: ")

def getCase(op, task = None):
    try:
        if op == "+" and task != None:
            addTask(task) # task is task
        elif op == "-" and task != None:
            removeTask(int(task)) # task is line number
        elif op == "/" and task != None:
            doneTask(int(task)) # task is line number
        elif op == 0 and task == None:
            exit()
        else:
            showHelp()
    except:
        print("Wrong option!")
        sleep(2)

createFiles()
while True:
    showMenu()
    inp = input("\n: ")

    if (inp == '0'):
        exit()

    inp = inp.split(' ')
    op = inp[0]
    task = ' '.join(inp[1:])
    getCase(op, task)
