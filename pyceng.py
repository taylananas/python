def triplets(max):
    lst = []
    for a in range(1,max):
        for b in range(a,max):
            for c in range(1,max):
                if ( a**2 + b**2 )== c**2:
                    lst.append((a,b,c))
    return lst

def palindromes(number):
    #if both binary and base-10 representation of range(number) is palindrome append that into a list
    lst = []
    for i in range(number):
        if str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i))[:1:-1]: 
            lst.append(i)
    return lst

def is_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    else: return True

def prime_factors(var):
    lst = []
    for z in range(2,var):
        if var%z == 0 and is_prime(z):
            lst.append(z)
    return lst

def matrix_mul(matrix_1,matrix_2): #! YANLIS matrix carpimi ogren oyle dene salak
    """
    >>> matrix_mul( [[1,2,3], [4,5,6], [7,8,9]], [[7,8,9], [4,5,6], [1,2,3]] )
    [[18, 24, 30], [54, 69, 84], [90, 114, 138]]
    """

    rows = len(matrix_1)
    columns = len(matrix_1[0])

    new_matrix = [[0]*rows for i in matrix_1]

    for i in range(rows):
        for z in range(columns):
            new_matrix[i][z] = matrix_1[i][z] * matrix_2[i][z]
            print(new_matrix)

    return new_matrix

def lis(lst):
    max_Temp = 1
    max = 0
    i = 0
    while i+1 < len(lst):
        if lst[i] <= lst[i+1]:
            max_Temp += 1
        else: 
            max = max_Temp
            max_Temp = 1
        i+=1
    return max
