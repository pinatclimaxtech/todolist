import io
import signal

todo_list = []
todoIndex = 0

def handler(signum, frame):
    exit (0)

signal.signal(signal.SIGINT, handler)

def add_todo_list(newJob):
    global todoIndex
    todoIndex += 1
    todo_list.append(newJob)

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
    print('-------------------')
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
        
    print('-------------------')


def validCommand():
    if len(todo_list) == 0:
        return False
    return True

inputBuffer = io.StringIO()
inputBuffer.write("1.Add a todo\n")
inputBuffer.write("2.Delete a todo\n")
inputBuffer.write("3.Check a todo\n")
inputBuffer.write("4.List all todos\n")

while True:
    todo = input(inputBuffer.getvalue())
    print('\n')

    if todo == "1":
        addAJob = input("add a job\n")
        add_todo_list(addAJob)
        print_todo_list()
    elif todo == "2":
        delAJob = input("input job number\n")
        remove_todo_list(delAJob)
        print_todo_list()
    elif todo == "3":
        checkAJob = input("input job number\n")
        check_todo(checkAJob)
        print_todo_list()
    elif todo == "4":
        print_todo_list()


