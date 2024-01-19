#Find the sum of first n natural numbers {1,2,3,...,n}

#ITERATIVE WAY
n = int(input("Insert a natural number."))

total = 0
for i in range(n+1): #this does not include n itself
    total += i
print("Iteratively, the total is", total)

#RECURSIVE WAY
def sumNnumbers(n):
    if n > 1:
        # print(n)
        return n + sumNnumbers(n-1)
    else:
        return n

print("Recursively, the total is",sumNnumbers(n))

#FIBONACCI
#0,1,1,2,3,5,8

def fiboNumber(n):
    if n <= 1:
        return n
    else:
        return fiboNumber(n-1) + fiboNumber(n-2)

print("The",n,"th fiboNumber is",fiboNumber(n))


#IMPLEMENTING RECURSION IN BINARY TREE
class Node:
    def __init__(self,val):
        self.val = val
        self.lbranch = None
        self.rbranch = None


# BINARY SORT
def insert(node,val):
    if node is None:
        return Node(val)
    else:
        if node.val is val:
            return node
        elif node.val < val:
            node.rbranch = insert(node.rbranch, val)
        else:
            node.lbranch = insert(node.lbranch, val)
    return node

def printBranches(node,path):
    path += " --> "+ str(node.val)
    haveBranch = False
    if node.lbranch:
        haveBranch = True
        printBranches(node.lbranch, path)
    if node.rbranch:
        haveBranch = True
        printBranches(node.rbranch, path)

    if not haveBranch:
        print(path)

def InOrderTraversal(node):
    if node.lbranch:
        InOrderTraversal(node.lbranch)
    print("-->", node.val, end=" ")
    if node.rbranch:
        InOrderTraversal(node.rbranch)


rootsort = Node(10)
insert(rootsort, 12)
insert(rootsort, 9)
insert(rootsort, 13)
insert(rootsort, 5)
insert(rootsort, 6)
insert(rootsort, 4)
insert(rootsort, 11)

printBranches(rootsort,"")
InOrderTraversal(rootsort)