class Node:
    def __init__(self,val):
        self.val = val
        self.lbranch = None
        self.rbranch = None

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


def printPreorder(node):
    if node:
        print("-->",node.val, end=" ")
        printPreorder(node.lbranch)
        printPreorder(node.rbranch)



root = Node(10)
insert(root,12)
insert(root,9)
insert(root,13)
insert(root,11)

print("Preorder")
printPreorder(root)
print("\nInorder")
printInorder(root)
print("\nPostorder")
printPostorder(root)