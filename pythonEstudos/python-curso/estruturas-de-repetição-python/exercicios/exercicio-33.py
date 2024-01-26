valor = int(input("Digite N: "))
j = 0
i = 0
while i == 0 or j == 0:
    i = int(input("Digite i: "))
    j = int(input("Digite j: "))
    if i == 0 or j == 0:
        print("Digite i e j != 0")
for k in range(valor+1):
    if k % i == 0:
        print(f"Multiplo de: {i}, {k}")
    elif k % j == 0:
        print(f"Multiplo de: {j}, {k}")
