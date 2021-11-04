from numpy import *

population = 2
a = 1

def formula(i, pop):
    R_factor = random.uniform(1.5,4)
    while pop < 10000:
        pop = pop * R_factor
        pop = round(pop)
        i += 1
        if i % 10 == 0 and pop < 10000:
            print(f"test {i}: {pop}, r: {R_factor}")
    print(f"{i}: {pop}, r: {R_factor}")

for i in range(40):
    formula(a,population)