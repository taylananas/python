def create_stack():
    return []

def push(item, stack):
    stack.append(item)

def pop(stack):
    return stack.pop()

def top(stack):
    return stack[-1]

def is_empty(stack):
    return stack == []