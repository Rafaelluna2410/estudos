def super_fatorial(n):
    mult = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            mult *= j
        
    return mult

print(super_fatorial(4))