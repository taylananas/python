def quadratic(a,b,c):
    kokler = ((-b + discriminant(a,b,c))/(2*a)), ((-b - discriminant(a,b,c))/(2*a))
    return kokler

def discriminant(a,b,c):
    dis = b**2 - 4*a*c
    return dis

a, b, c= input("a, b, c: ").split()
print(quadratic(float(a), float(b), float(c)))