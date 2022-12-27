def split(text, L):
    n = 0
    lst = []
    for i,value in enumerate(text):
        for j in L:
            if value == j:
                lst.append([text[n+1:i]])
                n = i
    if text[0] not in L:
        lst[0] = [text[0]]
    lst.append([text[n+1:]])
    return lst

def histogram(l, lenght): #!YANLIŞ
    new = []
    l = list(l)
    n=0
    for i,value in enumerate(l):
        if i%lenght == 0 and i != 0:
            new.append(l[n:i])
            n = i
    
    return new

def slice(l, start, end ,step):
    l = l[start:end]
    if end < 0:
        end = len(l) + end
    
    if start <0:
        start = len(l) +start
    
    if step > 0:
        return slicehelper(l,start,end,step)
    elif step < 0:
        l = reverser(l)
        return slicehelper(l,start,end,abs(step))
    
def reverser(l):
    if not l:
        return []
    
    else:
        return [l[-1]] + reverser(l[:-1])
    
def slicehelper(l,start,end,step):
    if not l:
        return []

    elif start < end:
        return [l[0]] + slicehelper(l[step:], start ,end ,step)
    
def is_substring(pattern, text):
    i = 0
    if not text:
        return False
    
    elif not pattern:
        return True
    
    else:
        part = len(pattern)
        return is_substring_helper(i,part,pattern,text)
        
def is_substring_helper(i, part, pattern, text):
    if pattern == text[i:i+part]:
        return True
    elif len(text[i:i+part])<len(pattern):
        return False
    else:
        return is_substring_helper(i+1,part,pattern,text)

def substrings(text):
    if len(text) == 0:
        return substrings(text)

    else:
        return [text[1:]] + substrings(text[1:])

print(substrings('ceng'))