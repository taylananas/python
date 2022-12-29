from abstracts import Stack, Queue

def fixsorted(lst):
    stack = Stack()
    lst.append("dummy element")
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            stack.push(lst[i])
        elif lst[i]<lst[i+1] and stack.stack:
            for x in range(stack.size()):
                lst.remove(stack.peek())
                lst.insert(i,stack.pop())
    lst.pop()
    return lst

roadlist = {
   "A": ["B", "C"],
   "B": ["F"],
   "C": ["D", "E"],
   "D": ["L"],
   "E": ["D"],
   "F": ["E", "G", "K"],
   "G": ["H"],
   "H": ["I", "J"],
   "I": ["L"],
   "J": ["L"],
   "K": [],
   "L": [],
}

def distance(lst, a, b):
    road = Queue()
    road.enqueue((a,0))
    for i in road.queue:
        for z in lst[i[0]]:
            road.enqueue((z,i[1]+1))

    for i in road.queue:
        if b in i[0]:
            return i[1]

print(distance(roadlist,"F","L"))