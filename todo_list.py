todo_list = {}
todoIndex = 0

def add_todo_list(newJob):
    global todoIndex
    todoIndex += 1
    todo_list[str(todoIndex)] = newJob

def remove_todo_list(jobNo):
    del todo_list[jobNo]
    return todo_list

def print_todo_list():
    print('list your todo here')
    print('-------------------')
    for key in todo_list:
        print(key, "->"  ,todo_list[key])


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
