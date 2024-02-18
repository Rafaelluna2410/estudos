def sao_anagramas(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    return True

string1 = "listen"
string2 = "silent"
print(sao_anagramas(string1, string2))

string3 = "hello55"
string4 = "world4"
print(sao_anagramas(string3, string4))
