import io
import signal

todo_list = []

def add_todo_list(newJob):
    todo_list.append(newJob)
    return todo_list

def remove_todo_list(jobNo):
    if int(jobNo) > len(todo_list):
        return todo_list
    
    todo_list.pop(int(jobNo)-1)
    return todo_list

def check_todo(jobNo):
    if int(jobNo) > len(todo_list):
        return todo_list
    
    checkBuffer = io.StringIO()
    jobIndex = int(jobNo)-1
    item = todo_list[jobIndex]
    for element in range(0, len(item)):
        checkBuffer.write("\u0336")
        checkBuffer.write(item[element])

    todo_list[jobIndex] = checkBuffer.getvalue()
    return todo_list


def print_todo_list():
    printBuffer = io.StringIO()
    print('YOUR TODOs')
    printDivider()
    for index, item in enumerate(todo_list):
        printBuffer.write(str(index+1))
        printBuffer.write(". ")
        printBuffer.write(item)
        if len(todo_list) != index+1:
            printBuffer.write("\n")

    if len(todo_list) == 0:
        print("without any todo")
    else:
        print(printBuffer.getvalue())
        
    printDivider()

def printDivider():
    for _ in range(20):
        print("-", end = "")
    print()

def validCommand():
    if len(todo_list) == 0:
        return False
    return True


def handler(signum, frame):
    exit (0)

signal.signal(signal.SIGINT, handler)

inputBuffer = io.StringIO()
inputBuffer.write("1.Add a todo\n")
inputBuffer.write("2.Delete a todo\n")
inputBuffer.write("3.Check a todo\n")
inputBuffer.write("other keys for print todos\n")

while True:
    todo = input(inputBuffer.getvalue())
    print()

    if todo == "1":
        addAJob = input("add a job\n")
        add_todo_list(addAJob)
    elif todo == "2":
        delAJob = input("input job number\n")
        remove_todo_list(delAJob)
    elif todo == "3":
        checkAJob = input("input job number\n")
        check_todo(checkAJob)
        print_todo_list()
    else:
        print_todo_list()
        continue

    print_todo_list()
