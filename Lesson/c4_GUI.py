import tkinter as tk
from functools import partial

###################
# THE LINKED LIST #
###################

# NODE CLASS
class Node:
    # CONSTRUCTOR
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    # BASIC USER-DEFINED OPERATIONS OF NODE
    def updateData(self, data):
        self.data = data

    def setLink(self, link):
        self.link = link

    def getData(self):
        return self.data

    def getNext(self):
        return self.link


# LINKED LIST CLASS
class LL:
    # LL CONSTRUCTOR
    def __init__(self,size):
        self.head = None
        self.maxSize = size

    # CLEARING THE LIST
    def clearList(self):
        self.head = None

    # GET THE LENGTH
    def length(self):
        current = self.head
        if current is None:
            return 0
        else:
            count = 0
            while current:
                count += 1
                current = current.getNext()
            del current
            return count

    # PUSH DATA INTO LIST
    def push(self, data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    # POP DATA FROM THE LIST
    def pop(self):
        tempNode = self.head
        if tempNode:
            self.head = tempNode.getNext()
            del tempNode

    # ENQUEUE DATA INTO LIST
    def enqueue(self, data):
        current = self.head
        if current is None:
            tempNode = Node(data)
            tempNode.setLink(self.head)
            self.head = tempNode
            del tempNode
        else:
            tempNode = Node(data)
            while current.getNext():
                current = current.getNext()
            current.setLink(tempNode)
            del tempNode
        del current

    # DEQUEUE DATA FROM THE LIST
    def dequeue(self):
        self.pop()

    # PRINT THE LIST IN THE CONSOLE
    def printList(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                print(current.getData(),end=" ")
                current = current.getNext()
                if current:
                    print("-->", end=" ")
        print()
        del current

    # REMOVE THE DATA BY FINDING IT'S INDEX
    def removebyIndex(self, index):
        current = self.head
        prev = None
        if current is None:
            print("List is empty")
        else:
            k = 0
            while current:
                if k == index:
                    print("Data", current.getData(), "at index", k, "will be removed")
                    if prev is None:
                        self.head = current.getNext()
                    else:
                        prev.setLink(current.getNext())

                    return
                else:
                    prev = current
                    current = current.getNext()
                    k += 1
            print("The index desired in not within the size of the list")

list = LL(12)


############################
# GIVING THE GUI FUNCTIONS #
############################

def clearInput():
   input.delete(0,'end')

def pushData():
    data = input.get()
    if data and list.length() != list.maxSize:
        list.push(data)
        clearInput()
        list.printList()
        showList()

def enqueueData():
    data = input.get()
    if data and list.length() != list.maxSize:
        list.enqueue(data)
        clearInput()
        list.printList()
        showList()

def popData():
    list.pop()
    list.printList()
    showList()

def dequeueData():
    list.dequeue()
    list.printList()
    showList()

def clearList():
    list.clearList()
    list.printList()
    showList()

def deleteData(i):
    print(i)
    list.removebyIndex(i)
    list.printList()
    showList()

def showList():
    current = list.head
    count = 0
    isList = False

    while current:
        isList = True
        data[count].config(text=current.getData())

        num[count].grid(row=count, column=0)
        data[count].grid(row=count, column=1, columnspan=3)
        delete[count].grid(row=count, column=5)

        count += 1
        current = current.getNext()

    while count < list.maxSize:
        data[count].config(text="")

        num[count].grid_forget()
        data[count].grid_forget()
        delete[count].grid_forget()
        count += 1

    if isList:
        listFrame.pack()
    else:
        listFrame.pack_forget()


####################
# CREATING THE GUI #
####################

# CREATE MAIN WINDOW
main = tk.Tk()
main.title('Stack and Queue Simulation')
main.resizable(width=False, height=False)

# CREATE INPUT FRAME
inputframe = tk.Frame(master=main, padx=10, pady=5)
inputframe.pack(fill=tk.X)

# CREATE INSTRUCTION TEXT
instruction = tk.Label(
    master=inputframe,
    text="Add data into the list either by \"PUSH\" or \"ENQUEUE\".\n"
         "Remove data from the list either by \"POP\" or \"DEQUEUE\".\n"
         f"Clear the list using \"CLEAR\". Max {list.maxSize} data only in this list.",
    width=50)
instruction.pack()

labelinput = tk.Label(master=inputframe, text="Input text\t")
labelinput.pack(side='left')

# CREATE INPUT BOX ELEMENT
input = tk.Entry(master=inputframe, width=50)
input.pack(side='right')

# CREATE BUTTON FRAME
buttonframe = tk.Frame(master=main, padx=10, pady=5)

# CREATE THE CLICKABLE BUTTON
pushButton = tk.Button(master=buttonframe, text="PUSH", width=10, command=pushData)
enqueueButton = tk.Button(master=buttonframe, text="ENQUEUE", width=10, command=enqueueData)
popButton = tk.Button(master=buttonframe, text="POP", width=10, command=popData)
dequeueButton = tk.Button(master=buttonframe, text="DEQUEUE", width=10, command=dequeueData)
clearButton = tk.Button(master=buttonframe, text="CLEAR", width=10, command=clearList)

pushButton.grid(row=0, column=0)
enqueueButton.grid(row=0, column=1)
popButton.grid(row=0, column=2)
dequeueButton.grid(row=0, column=3)
clearButton.grid(row=0, column=4)
buttonframe.pack()

# CREATING THE LIST
num = {}
data = {}
delete = {}
listFrame = tk.Frame(master=main, padx=10, pady=5)

for i in range(list.maxSize):
    num[i] = tk.Label(master=listFrame, text=str(i+1), width=11, height=2, relief='groove')
    data[i] = tk.Label(master=listFrame, text="", width=33, height=2, relief='groove')

    deleteData_arg = partial(deleteData, i)
    delete[i] = tk.Button(master=listFrame, text='Delete', width=10, command=deleteData_arg)

# RUN THE WINDOW
main.mainloop()
