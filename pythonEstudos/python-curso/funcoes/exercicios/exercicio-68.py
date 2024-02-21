def intercalada(str1, str2):
    nova_string = ''
    for i in range(len(str1)):
        nova_string += str1[i] + str2[i]

    return nova_string


str1 = 'rafael'
str2 = 'miguel'

print(intercalada(str1, str2))