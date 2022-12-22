def create_qu():
    return []

def enqu(item,qu):
    qu.append(item)

def dequ(qu):
    return qu.pop(0)

def front(qu):
    return qu[0]

def is_empty(qu):
    return qu == []

