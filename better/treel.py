def create_Node(value):
    return [value,[],[]]

def left(T):
    return T[1]

def right(T):
    return T[2]

def datum(T):
    return T[0]

def isEmpty(T):
    return T==[]

def insert(T, value):
    if isEmpty(T):
        T.extend(create_Node(value))
    
    elif value < datum(T):
        insert(left(T),value)
    
    elif value > datum(T):
        insert(right(T),value)

def preorderTreversal(T):
    tree=[]
    if isEmpty(T):
        return
    tree.append(datum(T))
    tree.append(preorderTreversal(left(T)))
    tree.append(preorderTreversal(right(T)))
    return tree

def inorderTreversal(T):
    tree = []
    if isEmpty(T):
        return None
    else:
        if not isEmpty(left(T)):
            tree += [inorderTreversal(left(T))]
        tree += [datum(T)]         
        if not isEmpty(right(T)):
            tree += [inorderTreversal(right(T))]

    return tree

            


a = []

insert(a,5)
insert(a,19)
insert(a,7)
insert(a,3)
insert(a,4)
insert(a,3.5)
insert(a,2.5)
print(a)
print(inorderTreversal(a))



