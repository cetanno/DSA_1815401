import tkinter as tk
import tkinter.font as tkFont
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
        if self.head:
            data = self.head.getData()
            self.head = None
            return data
        return ""

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
            data = tempNode.getData()
            del tempNode
            return data
        return ""

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
        return self.pop()

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
        if current is None: # IF THE LIST IS EMPTY
            return "", -1
        else:
            k = 0
            while current:
                if k == index:
                    data = current.getData()
                    if prev is None: # IF THE INDEX PROVIDED IS THE HEAD OF THE LIST
                        self.head = current.getNext()
                    else:
                        prev.setLink(current.getNext())

                    return data, k
                else: # IF THE INDEX IS OUTSIDE OF THE LIST
                    prev = current
                    current = current.getNext()
                    k += 1
            return "", -2

list = LL(10)


############################
# GIVING THE GUI FUNCTIONS #
############################

def clearInput():
    input.delete(0,'end')

def updateAction(text):
    action.config(text=text)
    action.pack(side="top")

def pushData():
    data = input.get()
    if data and list.length() != list.maxSize:
        list.push(data)
        updateAction(f"\"{data}\" has been pushed into the list.")
        clearInput()
        list.printList()
        showList()
    elif not data:
        updateAction(f"No data is given.")
    else:
        updateAction(f"The list is already full.")


def enqueueData():
    data = input.get()
    if data and list.length() != list.maxSize:
        list.enqueue(data)
        updateAction(f"\"{data}\" has been enqueued into the list.")
        clearInput()
        list.printList()
        showList()
    elif not data:
        updateAction(f"No data is given.")
    else:
        updateAction(f"The list is already full.")

def popData():
    data = list.pop()
    if data:
        updateAction(f"\"{data}\" has been popped from the list.")
        list.printList()
        showList()
    else:
        updateAction(f"You may not pop an empty list.")

def dequeueData():
    data = list.dequeue()
    if data:
        updateAction(f"\"{data}\" has been dequeued from the list.")
        list.printList()
        showList()
    else:
        updateAction(f"You may not dequeue an empty list.")

def clearList():
    data = list.clearList()
    if data:
        updateAction(f"The list has been cleared.")
        list.printList()
        showList()
    else:
        updateAction(f"The list is already empty.")

def deleteData(i):
    print(i)
    data, id = list.removebyIndex(i)
    if id == -1:
        updateAction(f"The list is already empty.")
    elif id == -2:
        updateAction(f"A bug has occurred here. This should not happen.")
    else:
        updateAction(f"\"{data}\" at position {id + 1} has been deleted from the list.")
        list.printList()
        showList()

def showList():
    current = list.head
    count = 0
    isList = False

    while current: # HANDLING THE POSITIONS THAT HOLD THE DATA
        isList = True
        data[count].config(text=current.getData())

        num[count].grid(row=count, column=0)
        data[count].grid(row=count, column=1, columnspan=3)
        delete[count].grid(row=count, column=5)

        count += 1
        current = current.getNext()

    while count < list.maxSize: # HANDLING EMPTY POSITIONS
        data[count].config(text="")

        num[count].grid_forget()
        data[count].grid_forget()
        delete[count].grid_forget()
        count += 1

    if isList: # CHECKING IF THE LIST EXIST OR NOT
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

# SETTING THE FONT
headerStyle = tkFont.Font(size=25,family="Times New Roman",weight="bold",underline=True,slant="italic")
contentStyle = tkFont.Font(size=15,family="Calibri")

# CREATE INSTRUCTION FRAME
instructionframe = tk.Frame(master=main, padx=10, pady=5)
instructionframe.pack(fill=tk.X)

# CREATE INSTRUCTION TEXT
header = tk.Label(master=instructionframe,text="STACK AND QUEUE SIMULATION", font= headerStyle)
instruction = tk.Label(
    master=instructionframe,
    text="Add data into the list either by \"PUSH\" or \"ENQUEUE\".\n"
         "Remove data from the list either by \"POP\" or \"DEQUEUE\".\n"
         f"Clear the list using \"CLEAR\". Max {list.maxSize} data only in this list.",
    font= contentStyle,
    width=50)
header.pack()
instruction.pack()

# CREATE ACTION TEXT
action = tk.Label(master= instructionframe,text="",font= contentStyle, width=50)

# CREATE INPUT FRAME
inputframe = tk.Frame(master=main, padx=10, pady=5)
inputframe.pack(fill=tk.X)

# CREATE INPUT LABEL
labelinput = tk.Label(master=inputframe, font= contentStyle,text="Input text\t")
labelinput.pack(side='left')

# CREATE INPUT BOX ELEMENT
input = tk.Entry(master=inputframe, font= contentStyle, width=40)
input.pack(side='right')

# CREATE BUTTON FRAME
buttonframe = tk.Frame(master=main, padx=10, pady=5)

# CREATE THE CLICKABLE BUTTONS
pushButton = tk.Button(master=buttonframe, font= contentStyle,text="PUSH", width=10, command=pushData)
enqueueButton = tk.Button(master=buttonframe, font= contentStyle,text="ENQUEUE", width=10, command=enqueueData)
popButton = tk.Button(master=buttonframe, font= contentStyle,text="POP", width=10, command=popData)
dequeueButton = tk.Button(master=buttonframe, font= contentStyle,text="DEQUEUE", width=10, command=dequeueData)
clearButton = tk.Button(master=buttonframe, font= contentStyle,text="CLEAR", width=10, command=clearList)

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
    num[i] = tk.Label(master=listFrame, font= contentStyle,text=str(i+1), width=11, height=2, relief='groove')
    data[i] = tk.Label(master=listFrame, font= contentStyle,text="", width=33, height=2, relief='groove')

    # ASSIGNING DISTINCT PARAMETRIC FUNCTIONAL COMMANDS (AKA CALLING SAME FUNCTION WITH INCREMENTAL VALUES) TO A BUTTON
    deleteData_arg = partial(deleteData, i) # deleteData(i)
    delete[i] = tk.Button(master=listFrame, font= contentStyle,text='Delete', width=10, command=deleteData_arg)

#   ANOTHER WAY TO PASS THE PARAMETER TO A COMMAND IS THE FOLLOWING CODE
#
#   delete[i] = tk.Button(master=listFrame, text='Delete', width=10, command= lambda : deleteData(i))
#
#   HOWEVER THIS ONLY APPLIES FOR NON-ARRAY COMPONENTS.


# RUN THE WINDOW
main.mainloop()

# TEAMWORK MAKES THE DREAM WORK
