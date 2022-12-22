class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,variable):
        self.stack.append(variable)
    
    def pop(self):
        if not self.isEmpty:
            return self.stack.pop()
        else:
            return None
            
    def peek(self):
        if not self.isEmpty:
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,variable):
        self.queue.append(variable)
    
    def dequeue(self):
        if not self.isEmpty:
            return self.queue.pop(0)
        else:
            return None
    
    def front(self):
        if not self.isEmpty:
            return self.queue[0]
        else:
            return None
    
    def isEmpty(self):
        return self.queue == []
    
    def size(self):
        return len(self.queue)