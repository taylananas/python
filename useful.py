def quadratic(a,b,c): #finds roots of a quadratic equation
    disc = discriminant(a,b,c)
    kokler = ((-b + disc)/(2*a)), ((-b - disc)/(2*a))
    return kokler

def discriminant(a,b,c): #finds discriminant of a quadratic equation
    dis = b**2 - 4*a*c
    return dis

def isprime(a): #checks if a number is prime
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def primefactors(a): #finds prime factors of a number
    factors = []
    for i in range(2, a):
        if a % i == 0:
            if isprime(i):
                factors.append(i)
    return factors

def kineticenergy(m,v): #finds kinetic energy of a moving object
    ke = 0.5*m*v**2
    return ke

def potentialenergy(m,g,h): #finds potential energy of an object
    pe = m*g*h
    return pe

