def sao_anagramas(str1, str2, caracteres):
    
    str1 += str2[0:caracteres]
    str2 += str1[0:caracteres]
    
    return f'{str1}, {str2}'

string1 = "listen"
string2 = "silent"
print(sao_anagramas(string1, string2, 2 ))

string3 = "hello"
string4 = "world4"
print(sao_anagramas(string3, string4, 3))
