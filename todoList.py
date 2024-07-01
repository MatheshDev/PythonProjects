print("Terminal Based To-Do List")
print("Syntax \n 1. create *taskname* - Creates a new Task \n 2. done *taskname* - Removes the Task from List \n")

taskList = []

def getCommand():
    while True:
        command = str(input("$ :- "))
        words = command.split()
        if(len(words) <= 0):
            print("Syntax Error")
            continue
        return list(words)
def addTask(task):
    taskList.append(task) 
def doneTask(task):
    taskList.remove(task)

while True:
    command = getCommand()

    if(command[0] == "create"):
        addTask(command[1::])
        for i in taskList:
            print(i)
    elif(command[0] == "done"):
        doneTask(command[1::])
        for i in taskList:
            print(i)
    else:
        print("Syntax Error")
        continue