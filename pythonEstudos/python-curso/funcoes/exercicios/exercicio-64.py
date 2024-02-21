def sao_anagramas(str1, str2):
    
    str1 += str2
    str2 += str1
    
    return f'{str1}, {str2}'

string1 = "listen"
string2 = "silent"
print(sao_anagramas(string1, string2))

string3 = "hello"
string4 = "world4"
print(sao_anagramas(string3, string4))
