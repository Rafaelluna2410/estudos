"""
Usando Fibonacci para test


"""
# Usando listas 449mb
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums



# Usando geradores  3MB

def fib_gen(max):
    a, b, contador = 0,1,0
    while contador < max:
        a, b = b, a+b
        yield a
        contador +=1

for n in fib_gen(100000):
    print(n)