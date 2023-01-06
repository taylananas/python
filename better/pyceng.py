def datum(tree):
    if not isempty(tree):
        return tree[0]

def append(tree,value):
    tree.extend(makenode(value))

def left(tree):
    return tree[1]

def right(tree):
    return tree[2]

def isempty(tree):
    return tree == []

def isleaf(tree):
    return left(tree) == [] and right(tree) == []

def makenode(datum):
    return [datum, [], []]

def countleaves(tree):
    if isempty(tree):
        return 0
    elif isleaf(tree):
        return 1
    else:
        return countleaves(left(tree)) + countleaves(right(tree))

def additem(tree,value):
    if isempty(tree):
        tree.extend(makenode(value))
    elif value < datum(tree):
        return additem(left(tree),value)
    elif value > datum(tree):
        return additem(right(tree),value)

def sumtree(tree):
    if isempty(tree):
        return 0
    elif isleaf(tree):
        return datum(tree)
    else:
        return datum(tree) + sumtree(left(tree)) + sumtree(right(tree))

def inorder(tree):
    if isempty(tree):
        return []
    else:
        return inorder(left(tree)) +  [datum(tree)] + inorder(right(tree))

def preorder(tree):
    if isempty(tree):
        return []
    else:
        return [datum(tree)] +  preorder(left(tree)) +  preorder(right(tree))

def isbinary(tree):
    if isempty(tree):
        return True
    elif isempty(left(tree)) and isempty(right(tree)):
        return True
    elif isempty(left(tree)) and not isempty(right(tree)):
        return True and isbinary(left(tree))
    elif not isempty(left(tree)) and isempty(right(tree)):
        return True and isbinary(right(tree))
    elif datum(tree) < datum(right(tree)) and datum(left(tree)) < datum(tree):
        return True and isbinary(right(tree)) and isbinary(left(tree))
    else:
        return False
    
def maxdepth(tree,depth=0):
    if isempty(tree):
        return depth
    else:
        return max(maxdepth(left(tree),depth+1), maxdepth(right(tree),depth+1))

def numparts(number):
    tree = []
    additem(tree,number)
    numpartshelper(tree,number)
    return tree

def numpartshelper(tree,number):
    parta = number-number//2
    partb = number//2
    if parta != 1:
        append(left(tree),parta)
        numpartshelper(left(tree),parta)
    elif parta == 1:
        append(left(tree),1)
        append(right(tree),1)
    
    if partb != 1:
        append(right(tree),partb)
        numpartshelper(right(tree),partb)
    elif partb == 1:
        append(left(tree),1)
        append(right(tree),1)

def checkmul(tree):
    if isempty(tree):
        return True
    elif isempty(left(tree)) or isempty(right(tree)):
        return True
    elif datum(left(tree)) * datum(right(tree)) == datum(tree):
        return True and checkmul(right(tree)) and checkmul(left(tree))
    else: return False

def build(tree):
    if isempty(tree):
        return
    elif datum(tree) == "string":
        return datum(left(tree)) + datum(right(tree))
    elif datum(tree) == "list":
        if datum(left(tree)) != "list" and datum(right(tree)) != "list":
            return [datum(left(tree)), datum(right(tree))]
        else:
            return [build(left(tree)), build(right(tree))]

        # if datum(left(tree)) != "list" and datum(right(tree)) == "list":
        #     return [datum(left(tree)), build(right(tree))]
        # if datum(left(tree)) == "list" and datum(right(tree)) != "list":
        #     return [build(left(tree)), datum(right(tree))]
        # if datum(left(tree)) == "list" and datum(right(tree)) == "list":
        #     return [build(left(tree)), build(right(tree))]
print(build(['list', ['string', ['ali'], ['veli']], ['list', ['string', ['ali'], ['veli']], ['b']]]))
print(build(['list', ['c'], ['eng']]))
print(build(['string', ['c'], ['eng']]))