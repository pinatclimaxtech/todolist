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
    todo_list.pop(int(jobNo)-1)
    return todo_list

def print_todo_list():
    buffer = io.StringIO()
    print('list your todo here')
    print('-------------------')
    for index, item in enumerate(todo_list):
        buffer.write(str(index+1))
        buffer.write(". ")
        buffer.write(item)
        if len(todo_list) != index+1:
            buffer.write("\n")

    print(buffer.getvalue())
    print('-------------------')


while True:
    todo = input("1.Add a job. \n2.Delete a job\n")
    print('\n')

    if todo == "1":
        addAJob = input("add a job here\n")
        add_todo_list(addAJob)
        print_todo_list()
    elif todo == "2":
        delAJob = input("input job number here\n")
        remove_todo_list(delAJob)
        print_todo_list()


