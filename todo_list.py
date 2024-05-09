import io
import signal

todo_list = []

class InterfAction:
    def add_todo_list(newJob): #C
        pass;
    def print_todo_list(): #R
        pass;
    def check_todo(jobNo): #U
        pass;
    def remove_todo_list(jobNo): #D
        pass;
    

class ImplAction:   
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def add_todo_list(self, newJob):
        self.todo_list.append(newJob)
        return self.todo_list

    def remove_todo_list(self, jobNo):
        if int(jobNo) > len(self.todo_list):
            return self.todo_list
        
        self.todo_list.pop(int(jobNo)-1)
        return self.todo_list

    def check_todo(self, jobNo):
        if int(jobNo) > len(self.todo_list):
            return self.todo_list
        
        checkBuffer = io.StringIO()
        jobIndex = int(jobNo)-1
        item = self.todo_list[jobIndex]
        for element in range(0, len(item)):
            checkBuffer.write("\u0336")
            checkBuffer.write(item[element])

        self.todo_list[jobIndex] = checkBuffer.getvalue()
        return self.todo_list


    def print_todo_list(self):
        printBuffer = io.StringIO()
        print('YOUR TODOs')
        printDivider()
        for index, item in enumerate(self.todo_list):
            printBuffer.write(str(index+1))
            printBuffer.write(". ")
            printBuffer.write(item)
            if len(todo_list) != index+1:
                printBuffer.write("\n")

        if len(self.todo_list) == 0:
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

implAction = ImplAction(todo_list)

while True:
    todo = input(inputBuffer.getvalue())
    print()

    if todo == "1":
        addAJob = input("add a job\n")
        implAction.add_todo_list(addAJob)
    elif todo == "2":
        delAJob = input("input job number\n")
        implAction.remove_todo_list(delAJob)
    elif todo == "3":
        checkAJob = input("input job number\n")
        implAction.check_todo(checkAJob)
        implAction.print_todo_list()
    else:
        implAction.print_todo_list()
        continue

    implAction.print_todo_list()
