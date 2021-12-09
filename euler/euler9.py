# a + b + c = 1000
# a^2 + b^2 = c^2
# a < b < c
# a.b.c = ?

def main():
    for c in range(1,1000):
        for b in range(1,1000-c):
            a = 1000 - (c + b)
            if a**2 + b**2 == c**2 and a<b<c:
                print(a,b,c)
                print(a*b*c)

if __name__ == '__main__':
    main()