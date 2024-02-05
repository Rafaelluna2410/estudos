def triangulo(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return f'Valor menor que 0'
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Equilatero'
        elif  a == b != c or b ==c != a:
            return 'Isósceles' 
        else:
            return 'Escaleno'
    else:
        return 'Os valores não formam um triângulo'
    
print(triangulo(5,45,95))
    