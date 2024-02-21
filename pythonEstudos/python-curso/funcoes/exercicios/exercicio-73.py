
def habitantes():

    caracteres_habitantes = []

    for i in range(5):
        informacoes = {'nome': '', 'sexo': '', 'olhos': '', 'cabelo': '', 'idade': 0}
        informacoes['nome'] = input('digite o nome do habitante: ')
        informacoes['sexo'] = input('digite o sexo do habitante: ')
        informacoes['olhos'] = input('digite a cor dos olhos do habitante: ')
        informacoes['cabelo'] = input('digite a cor do cabelo do habitante: ')
        informacoes['idade'] = int(input('digite a idade do habitante: '))
        caracteres_habitantes.append(informacoes)

    count= 0
    count_idade = 0
    maior_idade = 0

    quantidade_loiro_olhos_azuis = 0
    for i in range(len(caracteres_habitantes)):

        if caracteres_habitantes[i]["idade"] > maior_idade:
            maior_idade = caracteres_habitantes[i]["idade"]

        if caracteres_habitantes[i]["olhos"] == 'C' and caracteres_habitantes[i]["cabelo"] == "P":
            count += 1
            count_idade += caracteres_habitantes[i]["idade"]

        if caracteres_habitantes[i]["sexo"] == "F":
            if caracteres_habitantes[i]["idade"] >=18 and caracteres_habitantes[i]["idade"] <= 35:
                if caracteres_habitantes[i]["cabelo"] == "L" and caracteres_habitantes[i]["olhos"] == "A":
                    quantidade_loiro_olhos_azuis +=1

    #return f'Habitante {caracteres_habitantes[0]["nome"]}: {caracteres_habitantes[0]},\n  Habitante {caracteres_habitantes[1]["nome"]}: {caracteres_habitantes[1]}'
    return f"Media olhos castanho e cabelo preto: {count_idade/count},\n Maior idade: {maior_idade}, Loira >= 18 e <= 35: {quantidade_loiro_olhos_azuis}"
print(habitantes())
