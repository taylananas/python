def datum(tree):
    return tree[0]

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
    elif isleaf(tree):
        return [datum(tree)]
    else:
        return inorder(left(tree)) +  [datum(tree)] + inorder(right(tree))

def preorder(tree):
    if isempty(tree):
        return []
    elif isleaf(tree):
        return [datum(tree)]
    else:
        return [datum(tree)] +  inorder(left(tree)) +  inorder(right(tree))

