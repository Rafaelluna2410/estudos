
def data(data):
    parte = data.split('/')

    match parte[1]:
        case '01':
            return f'data: {parte[0]} janeiro de {parte[2]}'
        case '02':
            return f'data: {parte[0]} fevereiro de {parte[2]}'
        case '03':
            return f'data: {parte[0]} março de {parte[2]}'
        case '04':
            return f'data: {parte[0]} abril de {parte[2]}'
        case '05':
            return f'data: {parte[0]} maio de {parte[2]}'
        case '06':
            return f'data: {parte[0]} junho de {parte[2]}'
        case '07':
            return f'data: {parte[0]} julho de {parte[2]}'
        case '08':
            return f'data: {parte[0]} agosto de {parte[2]}'
        case '09':
            return f'data: {parte[0]} setembro de {parte[2]}'
        case '10':
            return f'data: {parte[0]} outubro de {parte[2]}'
        case '11':
            return f'data: {parte[0]} novembro de {parte[2]}'
        case '12':
            return f'data: {parte[0]} dezembro de {parte[2]}'
        
    return f'Passou algo errado'

print(data('01/02/2000'))