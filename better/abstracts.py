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

