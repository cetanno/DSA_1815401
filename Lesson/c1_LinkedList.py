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
            return 0
        else:
            count = 0
            while current:
                count += 1
                current = current.getNext()
            return count
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
        print()
        del current

    #GET THE MAX VALUE
    def max(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            max = current.getData()
            while current.getNext():
                current = current.getNext()
                if current.getData() > max:
                    max = current.getData()
            return max
        del current

    # GET THE MAX VALUE
    def min(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            min = current.getData()
            while current.getNext():
                current = current.getNext()
                if current.getData() < min:
                    min = current.getData()
            return min
        del current

    #CALCULATE THE RANGE
    def rangeOptimized(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            max = current.getData()
            min = current.getData()
            while current.getNext():
                current = current.getNext()
                if current.getData() < min:
                    min = current.getData()
                if current.getData() > max:
                    max = current.getData()
            return max - min
        del current

    def range(self):
        if self.head is None:
            print("List is empty")
        else:
            return self.max() - self.min()

    #CALCULATE THE TOTAL
    def total(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            sum = current.getData()
            while current.getNext():
                current = current.getNext()
                sum += current.getData()
            return sum
        del current

    #CALCULATE THE AVERAGE
    def average(self):
        if self.head is None:
            print("List is empty")
        else:
            return self.total() / self.length()

    #CHECK THE ORDER OF THE LIST
    def checkSort(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            increase = False
            decrease = False
            k = current.getData()
            while current.getNext():
                current = current.getNext()
                if current.getData() > k:
                    increase = True
                elif current.getData() < k:
                    decrease = True
                k = current.getData()
            if (increase and decrease or (not increase and not decrease)):
                print ("Neither")
            elif (increase):
                print ("Increase")
            else:
                print("Decrease")
        del current

    # SORT IN INCREASING ORDER
    def sortIncrease(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                tempNode = current.getNext()
                while tempNode:
                    if tempNode.getData() < current.getData():
                        tempValue = current.getData()
                        current.updateData(tempNode.getData())
                        tempNode.updateData(tempValue)
                    tempNode = tempNode.getNext()
                current = current.getNext()
            print ("The list is sorted in increasing order.")

    #SORT IN DECREASING ORDER
    def sortDecrease(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                tempNode = current.getNext()
                while tempNode:
                    if tempNode.getData() > current.getData():
                        tempValue = current.getData()
                        current.updateData(tempNode.getData())
                        tempNode.updateData(tempValue)
                    tempNode = tempNode.getNext()
                current = current.getNext()
            print ("The list is sorted in decreasing order.")

    #FIND THE DATA IN THE LIST
    def findData(self,data):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            k = 1
            while current:
                if current.getData() == data:
                    print("The data is found in the list at index", k)
                    return k
                current = current.getNext()
                k += 1
            print("The data is not found in the list.")

    #HOW TO GET DATA USING THE INDEX
    def getData(self,index):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            k = 1
            while current:
                if k == index:
                    print("The data at index", k, "is", current.getData())
                    return current.getData()
                current = current.getNext()
                k += 1
            print("The index desired in not within the size of the list")

    #REMOVE THE DATA BY FINDING IT'S INDEX
    def removebyIndex(self,index):
        current = self.head
        prev = None
        if current is None:
            print("List is empty")
        else:
            k = 1
            while current:
                if k == index:
                    print("Data", current.getData(),"at index", k,"will be removed")
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

#IMPLEMENT SEVERAL FUNCTIONS INTO LINKED LIST CLASS ABOVE (PRACTICE 1, DONE)
# Get the maximum value from the list
# Get the minimum value from the list
# Get the range value from the list
# Get the total and average value from the list
# Check whether the list is sorted in increasing or decreasing or neither

#IMPLEMENT SEVERAL FUNCTIONS INTO LINKED LIST CLASS ABOVE (PRACTICE 2)
# Modify the removebyIndex to create another function removeData that removes the data by searching for the data in the list.
# CHALLENGE
# Insert the data into a sorted list while keeping it sorted (increasing or decreasing), if the list is not sorted, abort the operation.

list = LL()
list.push(1)
list.push(2)
list.push(3)
list.push(4)

list.displayList()
print(list.max())
print(list.min())

print(list.range())
print(list.rangeOptimized()) #not recommended in some cases
print(list.total())
print(list.average())

list.checkSort()

list.sortIncrease()
list.displayList()

list.sortDecrease()
list.displayList()

list.findData(3)
list.findData(5)

list.getData(3)
list.getData(5)

list.removebyIndex(2)
list.removebyIndex(4)
list.displayList()
