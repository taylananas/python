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

def path_exists(tree,path):
    if isempty(tree):
        return False
    if isempty(path):
        return True
    elif len(path) == 1:
        if datum(tree) == path:
            return True
        elif datum(left(tree)) == path:
            return True
        elif datum(right(tree)) == path:
            return True
        else:
            return False
    elif path[0] == datum(tree):
        return True and (path_exists(left(tree),path[1:]) or path_exists(right(tree),path[1:]))
    elif path[0] != datum(tree):
        return (path_exists(left(tree),path[1:]) or path_exists(right(tree),path[1:]))

# print(path_exists(['a', ['b', ['c', [], []], ['d', [], []]], ['e', [], []]], 'bc'))
# print(path_exists(['a', ['b', ['c', [], []], ['d', ['1', [], []], ['2', [], []]]], ['e', [], []]], 'bd'))
# print(path_exists(['a', ['b', ['c', [], []], ['d', [], []]], ['e', [], []]], 'abd'))
# print(path_exists(['a', ['b', ['c', [], []], ['d', ['k', [], []], []]], ['e', [], []]], 'abe'))
# print(path_exists(['a', ['b', ['c', [], ['g', [], []]], ['d', [], []]], ['e', ['f'], []]], 'ae'))
def build(tree): #! CALISMIYOR
    if isempty(tree):
        return
    elif datum(tree) == "string":
        return datum(left(tree)) + datum(right(tree))
    elif datum(tree) == "list":
        if datum(left(tree)) != "list" and datum(right(tree)) != "list" and datum(left(tree)) != "string" and datum(right(tree)) != "list":
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

def path_has_sum(tree,sum,sum2 = 0):
    if sum2 == sum:
        return True

    if not isempty(tree):
        sum2 += datum(tree)

    if sum2 == sum:
        return True
    if (left(tree)) and (right(tree)):
        if sum2 > sum:
            return (path_has_sum(left(tree),sum,sum2=0) or path_has_sum(right(tree),sum,sum2=0))
        elif sum2 < sum:
            return (path_has_sum(left(tree),sum,sum2) or path_has_sum(right(tree),sum,sum2) or\
                path_has_sum(left(tree),sum,sum2=0) or path_has_sum(right(tree),sum,sum2=0))

    elif (left(tree)) and (not (right(tree))):
        if sum2 > sum:
            return (path_has_sum(left(tree),sum,sum2=0))
        elif sum2 < sum:
            return (path_has_sum(left(tree),sum,sum2) or path_has_sum(left(tree),sum,sum2=0))

    elif (not (left(tree))) and (right(tree)):
        if sum2 > sum:
            return path_has_sum(right(tree),sum,sum2=0)
        elif sum2 < sum:
            return (path_has_sum(right(tree),sum,sum2) or path_has_sum(right(tree),sum,sum2=0))

    elif (not (left(tree))) and (not (right(tree))):
        return sum2 == sum

# print(path_has_sum([1, [6, [3, [], []], []], [4, [], []]], 4))
# print(path_has_sum([1, [6, [], []], [4, [], []]], 5))
# print(path_has_sum([1, [6, [], []], [4, [2, [], []], [3, [2, [], []], []]]], 16))
# print(path_has_sum([1, [6, [], []], [4, [2, [], []], [3, [], []]]], 4))