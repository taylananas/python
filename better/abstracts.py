class Stack:
    def __init__(self):
        self.stack = []
    
    def append(self,variable):
        self.stack.append(variable)
    
    def pop(self):
        return self.stack.pop()
    
    def next_item(self):
        return self.stack[-1]
    
    def is_empty(self):
        return self.stack == []

class Queue:
    def __init__(self):
        self.queue = []
    
    def append(self,variable):
        self.queue.append(variable)
    
    def pop(self):
        return self.queue.pop(0)
    
    def next_item(self):
        return self.queue[0]
    
    def is_empty(self):
        return self.queue == []


class Tree:
    def __init__(self,root):
        self.root = root
        self.left = None
        self.right = None

    def insert(self, value):
        if value == self.root:
            return
        
        elif value < self.root:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Tree(value)

        elif value > self.root:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Tree(value)
        
        else:
            self.root = value

    def search(self,value,depth=0):
        if self.root == None:
            return False

        elif value == self.root:
            return depth
        
        elif value < self.root:
            if self.left:
                depth +=1
                return self.left.search(value,depth)
            else: return False
        
        elif value > self.root:
            if self.right:
                depth +=1
                return self.right.search(value,depth)
            else: return False

    def printTree(self):
        print(self.root)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

    def inorderTreversal(self,node):
        tree = []
        if node:
            tree = self.inorderTreversal(node.left)
            tree.append(node.root)
            tree += self.inorderTreversal(node.right)
        return tree

    def preorderTreversal(self,node):
        tree = []
        if node:
            tree.append(node.root)
            tree += self.preorderTreversal(node.left)
            tree += self.preorderTreversal(node.right)
        return tree


    
a=Tree(10)

a.insert(5)
a.insert(12)
a.insert(1)
a.insert(11)
a.insert(10)
a.insert(19)
a.insert(23)
a.insert(25)
print(a.search(25))
print(a.inorderTreversal(a))
print(a.preorderTreversal(a))
a.printTree()