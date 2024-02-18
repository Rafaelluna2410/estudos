def sao_anagramas(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    contador_str1 = {}
    contador_str2 = {}
    
    for char in str1:
        contador_str1[char] = contador_str1.get(char, 0) + 1
    
    for char in str2:
        contador_str2[char] = contador_str2.get(char, 0) + 1
    
    print(contador_str1)
    print(contador_str2)
    return contador_str1 == contador_str2

string1 = "listen"
string2 = "silent"
print(sao_anagramas(string1, string2))

string3 = "hello"
string4 = "world"
print(sao_anagramas(string3, string4))
