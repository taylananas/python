#and gate, i and j == 1: return 1

def and_gate():
    for i in range(2):
        for j in range(2):
            print(f"{i}  {j} = {i and j}")

def triangle(h):
    for i in range(h):
        if i%2 == 0:
            print(f"{(h-i)*' '}{i*'*'}")
        else:
            print(f"{(h-i)*' '}{i*'*'}")

triangle(10)