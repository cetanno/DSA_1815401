class Node:
    def __init__(self,val):
        self.val = val
        self.lbranch = None
        self.rbranch = None

def printPreorder(node):
    if node:
        print("-->",node.val, end=" ")
        printPreorder(node.lbranch)
        printPreorder(node.rbranch)

def printInorder(node):
    if node:
        printInorder(node.lbranch)
        print("-->",node.val, end=" ")
        printInorder(node.rbranch)

def printPostorder(node):
    if node:
        printPostorder(node.lbranch)
        printPostorder(node.rbranch)
        print("-->",node.val, end=" ")


root = Node(1)
root.rbranch = Node(2)
root.lbranch = Node(3)
root.rbranch.rbranch = Node(4)
root.rbranch.lbranch = Node(5)

print("Preorder")
printPreorder(root)
print("\nInorder")
printInorder(root)
print("\nPostorder")
printPostorder(root)
print()


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

rootsort = Node(10)
insert(rootsort, 12)
insert(rootsort, 9)
insert(rootsort, 13)
insert(rootsort, 11)

print("Preorder")
printPreorder(rootsort)
print("\nInorder")
printInorder(rootsort)
print("\nPostorder")
printPostorder(rootsort)