import tkinter as tk

###################
# THE LINKED LIST #
###################

# NODE CLASS
class Node:
    # CONSTUCTOR
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
    def __init__(self):
        self.head = None

    # CLEARING THE LIST
    def clearList(self):
        self.head = None

    # PUSH DATA INTO LIST
    def push(self, data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    # POP DATA FROM THE LIST
    def pop(self):
        tempNode = self.head
        self.head = tempNode.getNext()
        del tempNode

    # ENQUEUE DATA INTO LIST
    def enqueue(self, data):
        current = self.head
        if current is None:
            self.addToStart(data)
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

    # REMOVE THE DATA BY FINDING IT'S INDEX
    def removebyIndex(self, index):
        current = self.head
        prev = None
        if current is None:
            print("List is empty")
        else:
            k = 1
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

list = LL()

####################
# CREATING THE GUI #
####################

# CREATE MAIN WINDOW
main = tk.Tk()
main.title('Stack and Queue Simulation')
main.resizable(width=False, height=True)

# CREATE INPUT FRAME
inputframe = tk.Frame(master=main, padx=10, pady=5)
inputframe.pack(fill=tk.X)

# CREATE INSTRUCTION TEXT
instruction = tk.Label(
    master=inputframe,
    text="Add data into the list either by \"PUSH\" or \"ENQUEUE\".\n"
         "Remove data from the list either by \"POP\" or \"DEQUEUE\".\n"
         "Clear the list using \"CLEAR\".",
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
pushButton = tk.Button(master=buttonframe, text="PUSH", width=10)
enqueueButton = tk.Button(master=buttonframe, text="ENQUEUE", width=10)
popButton = tk.Button(master=buttonframe, text="POP", width=10)
dequeueButton = tk.Button(master=buttonframe, text="DEQUEUE", width=10)
clearButton = tk.Button(master=buttonframe, text="CLEAR", width=10)

pushButton.grid(row=0, column=0)
enqueueButton.grid(row=0, column=1)
popButton.grid(row=0, column=2)
dequeueButton.grid(row=0, column=3)
clearButton.grid(row=0, column=4)
buttonframe.pack()

# RUN THE WINDOW
main.mainloop()
