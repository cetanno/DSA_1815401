#NODE CLASS
class Node:
    #CONSTUCTOR
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    #BASIC USER-DEFINED OPERATIONS OF NODE

    def updateData(self,data):
        self.data = data

    def setLink(self,link):
        self.link = link

    def removeLink(self):
        self.link = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.link

#LINKED LIST CLASS
class LL:
    #LL CONSTRUCTOR
    def __init__(self):
        self.head = None

    #ADD A NODE TO THE START OF THE LIST
    def addToStart(self,data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    #ADD A NODE TO THE END OF THE LIST
    def addToEnd(self,data):
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

    #CLEARING THE LIST
    def clearList(self):
        self.head = None

    #GET THE LENGTH
    def length(self):
        current = self.head
        if current is None:
            print("0")
        else:
            count = 0
            while current:
                count += 1
                current = current.getNext()
            print(count)
        del current

    #PUSH DATA INTO LIST
    def push(self,data):
        self.addToStart(data)
        #WHAT IT DOES
        # tempNode = Node(data)
        # tempNode.setLink(self.head)
        # self.head = tempNode
        # del tempNode

    #POP DATA FROM THE LIST
    def pop(self):
        tempNode = self.head
        self.head = tempNode.getNext()
        del tempNode

    #ENQUEUE DATA INTO LIST
    def enqueue(self,data):
        self.addToEnd(data)
        #WHAT IT DOES
        # current = self.head
        # if current is None:
        #     self.addToStart(data)
        # else:
        #     tempNode = Node(data)
        #     while current.getNext():
        #         current = current.getNext()
        #     current.setLink(tempNode)
        #     del tempNode
        # del current

    #DEQUEUE DATA FROM THE LIST
    def dequeue(self):
        self.pop()
        #WHAT IT DOES
        # tempNode = self.head
        # self.head = tempNode.getNext()
        # del tempNode

    #DISPLAY THE LINKED LIST
    def displayList(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                print(current.getData(),end=" ")
                current = current.getNext()
                if current:
                    print("-->", end=" ")
        del current

#IMPLEMENT SEVERAL FUNCTIONS INTO LINKED LIST CLASS ABOVE
# Get the maximum value from the list
# Get the minimum value from the list
# Get the range value from the list
# Get the total and average value from the list
# Check whether the list is sorted in increasing or decreasing or neither


list = LL()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)
list.displayList()
list.pop()
list.pop()
list.displayList()

list.clearList()
list.displayList()

list.enqueue(1)
list.enqueue(2)
list.enqueue(3)
list.enqueue(4)
list.enqueue(5)
list.displayList()
list.dequeue()
list.dequeue()
list.displayList()