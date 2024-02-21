def calculadora(a, b, tipo):
    match tipo:
        case '+':
            return a +b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
    return 'Foi digitado algo errado' 

print(calculadora(3,4, '*'))
print(calculadora(3,4, '+'))
print(calculadora(3,4, '/'))
print(calculadora(3,4, '-'))