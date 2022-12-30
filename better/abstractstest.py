from abstracts import Stack, Queue

def schedule():
    q = Queue()
    q.enqueue((1,"John"))
    q.enqueue((5,"George"))
    q.enqueue((1,"Lucy"))
    q.enqueue((2,"Arnold"))
    q.enqueue((3,"William"))
    q.enqueue((4,"Claude"))
    i = 1
    cant =[]
    while True:
        if not q.isEmpty():
            if i <= q.front()[0]:
                i += 1 
                q.dequeue()
            else:
                cant.append(q.dequeue())
        else:
            return cant

# print(schedule())

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
    alllll= []
    while not road.isEmpty():
        print(road.queue)
        first = road.dequeue()
        if first[0] != b:
            key = first[0]
            dist = first[1]
            for i in lst[key]:
                road.enqueue((i,dist+1))
        else:
            alllll.append(first[1]+1)
    return (alllll)
    

print(distance(roadlist,"B","L"))

def flatten(lst):
    finallist=[]
    for i in lst:
        if type(i) != list:
            finallist.append(i)
        else:
            tempqueue = Queue()
            for z in i:
                tempqueue.enqueue(z)
            while not tempqueue.isEmpty():
                print(tempqueue.queue)
                first = tempqueue.dequeue()
                print(finallist)
                if type(first) != list:
                    finallist.append(first)
                else:
                    for z in first:
                        tempqueue.enqueue(z)
    return finallist

print(flatten([1,2,3,[4,5,[6,7,[8,9],10,11],12],13]))
