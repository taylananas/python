import stack
import qu
import pdb
def check_parantheses(s):
    st = stack.create_stack()
    openers = ["(","[","{"]
    closers = [")","]","}"]
    for c in s:
        if c in openers:
            stack.push(c,st)
        elif c in closers:
            print(st)
            if stack.is_empty(st):
                return False
            elif closers.index(c) != openers.index(stack.pop(st)):
                return False
    if not stack.is_empty(st):
        return False
    return True

def flatten(lst):
    flatted_list = []
    q = qu.create_qu()
    for element in lst:
        qu.enqu(element,q) # dump all elements into a queue
    
    while (not qu.is_empty(q)):
        first = qu.dequ(q) # take the first element of queue
        if type(first) == list: #if the element is a queue, dump all list elements into queue
            for e in first:
                qu.enqu(e,q)
        else: 
            flatted_list.append(first) #if not a list, append it to final list
    return flatted_list

def binary_search(lst,element):
    check = True
    steps = 1
    while len(lst) > 1:
        print(steps)
        steps += 1
        lenght = len(lst)
        if element == lst[lenght//2]:
            return True
        elif element < lst[lenght//2]:
            lst = lst[:lenght//2]
        else: 
            lst = lst[lenght//2:]
    else: 
        return False

print(binary_search(list(range(2**22)),8192))
