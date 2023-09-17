import os

username = os.environ.get('USERNAME')


print(f"Username: {username}")

##outra forma de adicionar a variável na string
#mensagem = "nome do user: {}".format(username)
#
#print(mensagem)

#diretório


#
#os.chdir('/home')
#os.mkdir('pythondir')
#print(f"Dir current: {dir_current}")

os.system('cd /home/rafael')
os.system('mkdir luna')
dir_current = os.getcwd()
print(f"Dir current: {dir_current}")