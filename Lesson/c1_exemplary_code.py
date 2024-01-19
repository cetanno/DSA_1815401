# NODE CLASS
class Node:
    # CONSTRUCTOR
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    def updateData(self, data):
        self.data = data

    def setLink(self, link):
        self.link = link

    def removeLink(self):
        self.link = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.link


# LINKED LIST CLASS
class LL:
    # LL CONSTRUCTOR
    def __init__(self):
        self.head = None

    # Task2a (addtoStart, count, displayList)
    def addToStart(self, data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode

    def count(self):
        current = self.head
        if current is None:
            return 0
        else:
            count = 0
            while current:
                count += 1
                current = current.getNext()
            return count

    def displayList(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                print(current.getData(), end=" ")
                current = current.getNext()
                if current:
                    print("-->", end=" ")
        print()

    # Task2b (countOdd, countEven)
    def countOdd(self):
        count = 0
        current = self.head
        if current is None:
            return count
        else:
            while current:
                if current.data % 2 != 0:
                    count += 1
                current = current.getNext()
        return count

    def countEven(self):
        count = 0
        current = self.head
        if current is None:
            return count
        else:
            while current:
                if current.data % 2 == 0:
                    count += 1
                current = current.getNext()
        return count

    # Task2c (swap 2 element via index)
    def swap(self, index1, index2):
        length = self.count()

        if index1 < 0 or index1 >= length or index2 < 0 or index2 >= length:
            print("Error: Invalid index values for swapping.")
            return

        prev1, current1 = None, self.head
        for i in range(index1):
            prev1, current1 = current1, current1.getNext()

        prev2, current2 = None, self.head
        for i in range(index2):
            prev2, current2 = current2, current2.getNext()

        if prev1:
            prev1.setLink(current2)
        else:
            self.head = current2

        if prev2:
            prev2.setLink(current1)
        else:
            self.head = current1

        temp = current1.getNext()
        current1.setLink(current2.getNext())
        current2.setLink(temp)

    # Task2d (max, min, range, total, average)
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

    def range(self):
        if self.head is None:
            print("List is empty")
        else:
            return self.max() - self.min()

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

    def average(self):
        if self.head is None:
            print("List is empty")
        else:
            return self.total() / self.count()

    # CHALLENGE
    # Insert the data into a sorted list while keeping it sorted (increasing or decreasing),
    # if the list is not sorted, abort the operation.
    # approachA: use checksort to check if sorted, if not, abort. then addtostart new data, then sortAscend or sortDescend based on original state
    # approachB: after checksort, traverse link to find correct position, create new node then adjust link

    def checkSort(self):
        current = self.head
        if current is None:
            print("List is empty")
            sort = "Neither"
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
                sort = "Neither"
            elif (increase):
                sort = "Increase"
            else:
                sort = "Decrease"
        return sort

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

                # approach A

    def insertToSortedListA(self, data):
        sort = self.checkSort()
        if sort == "Neither":
            print("Aborted, list is empty or unsorted.")
        elif sort == "Increase":
            self.addToStart(data)
            self.sortIncrease()
        else:
            self.addToStart(data)
            self.sortDecrease()

    # approach B
    def insertToSortedListB(self, data):
        sort = self.checkSort()
        new_node = Node(data)
        if sort == "Neither":
            print("Aborted, list is empty or unsorted.")
        elif sort == "Increase":
            if data < self.head.getData():
                new_node.setLink(self.head)
                self.head = new_node
                return
            current = self.head
            while current.getNext() and current.getNext().getData() < data:
                current = current.getNext()
            new_node.setLink(current.getNext())
            current.setLink(new_node)
        else:
            if data > self.head.getData():
                new_node.setLink(self.head)
                self.head = new_node
                return
            current = self.head
            while current.getNext() and current.getNext().getData() > data:
                current = current.getNext()
            new_node.setLink(current.getNext())
            current.setLink(new_node)


# Appended Code
list = LL()
list.addToStart(10)
list.addToStart(20)
list.addToStart(45)
list.addToStart(35)
list.addToStart(15)
list.displayList()
print(list.count())
print(list.countOdd())
print(list.countEven())
list.addToStart(30)
list.addToStart(40)
list.displayList()
print(list.count())
print(list.countOdd())
print(list.countEven())
list.swap(1, 5)
list.displayList()
list.swap(2, 3)
list.displayList()
list.swap(7, 4)
list.displayList()
print(list.max())
print(list.min())
print(list.range())
print(list.total())
print(list.average())

# # Challenge test code
print("Test for unsorted input. (4,7,3,1)")
unsorted = LL()
unsorted.addToStart(1)
unsorted.addToStart(3)
unsorted.addToStart(7)
unsorted.addToStart(4)
unsorted.insertToSortedListA(6)
print("List (unsorted) after insertion:")
unsorted.displayList()

print("\nTest for sorted ascending input. (1,3,5,7)")
sortedAsc = LL()
sortedAsc.addToStart(7)
sortedAsc.addToStart(5)
sortedAsc.addToStart(3)
sortedAsc.addToStart(1)
sortedAsc.displayList()
sortedAsc.insertToSortedListA(2)
print("List (sortedAsc) after insertion:")
sortedAsc.displayList()
sortedAsc.insertToSortedListA(5)
print("List (sortedAsc) after insertion:")
sortedAsc.displayList()
sortedAsc.insertToSortedListB(0)
print("List (sortedAsc) after insertion:")
sortedAsc.displayList()
sortedAsc.insertToSortedListB(7)
print("List (sortedAsc) after insertion:")
sortedAsc.displayList()
sortedAsc.insertToSortedListB(9)
print("List (sortedAsc) after insertion:")
sortedAsc.displayList()

print("\nTest for sorted descending input. (7,3,2,1)")
sortedDesc = LL()
sortedDesc.addToStart(1)
sortedDesc.addToStart(2)
sortedDesc.addToStart(3)
sortedDesc.addToStart(7)
sortedDesc.displayList()
sortedDesc.insertToSortedListA(8)
print("List (sortedDesc) after insertion:")
sortedDesc.displayList()
sortedDesc.insertToSortedListA(5)
print("List (sortedDesc) after insertion:")
sortedDesc.displayList()
sortedDesc.insertToSortedListB(0)
print("List (sortedDesc) after insertion:")
sortedDesc.displayList()
sortedDesc.insertToSortedListB(7)
print("List (sortedDesc) after insertion:")
sortedDesc.displayList()
sortedDesc.insertToSortedListB(2)
print("List (sortedDesc) after insertion:")
sortedDesc.displayList()