from functools import reduce

a = [-4,6,8,-3,2,5,7,11,13,31,33,11,21,11]
#map(function, iterable) applies function to each element of iterable
abs_a = list(map(abs, a))

def isprime(a):
    for i in range(2,a):
        if a%i == 0:
            return 0
    return 1

#filter(function, iterable) if function returns true, the element is kept
#isprime_a = list(filter(isprime, abs_a))


def factorial(a): #iterative factorial using reduce
    if a == 0:
        return 1
    else:
        return reduce(lambda a,b: a*b , range(1,a+1)) #reduce(function, iterable) applies function to each element of iterable and returns the result

def rec_factorial(a): #recursive factorial
    if a == 0:
        return 1
    else:
        return a*rec_factorial(a-1)

def reversal(lst): #recursive list reversal
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reversal(lst[:-1])

def count_elements(element ,lst): #recursive element counter
    if not lst:
        return 0
    else:
        if element == lst[0]:
            return 1+count_elements(element,lst[1:])
        else:
            return count_elements(element,lst[1:])

def even_indexes(lst): #returns even indexes of a list
    if len(lst)==0: return []
    elif len(lst)%2 == 0: return even_indexes(lst[:-1])
    else: return even_indexes(lst[:-1]) +[lst[-1]]

def keep_numbers(lst): 
    if len(lst) == 0: return []
    elif type(lst[0]) == int: return [lst[0]] + keep_numbers(lst[1:])
    else: return keep_numbers(lst[1:])

def manual_filter(typeVar, lst):
    if not lst: return []
    elif typeVar(str(lst[0])): return [lst[0]] + manual_filter(typeVar, lst[1:])
    else: return manual_filter(typeVar,lst[1:])

def fibonacci(last):
    if last == 0: return [0]
    elif last == 1: return [0,1]
    else:
        fib = fibonacci(last-1)
        return fib + [fib[-1]+fib[-2]]

print(fibonacci(100))