import datetime
import paramiko
from paramiko import SSHClient


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='30.30.30.244', port='22', username='rafael',password='admin123')
scp = ssh.open_sftp()

day = datetime.date.today()

name_day = day.strftime('%A')
print(name_day)

match name_day:
    case 'Monday':
        scp.put(localpath='C:\\Users\\pc\\Desktop\\teste\\teste.txt', remotepath= '/home/rafael/teste.txt')
        scp.close()
        ssh.close()
        print("It's Monday!")#segunda
    case 'Tuesday':
        scp.put(localpath='C:\\Users\\pc\\Desktop\\teste\\teste.txt', remotepath= '/home/rafael/teste.txt')
        scp.close()
        ssh.close()
        print("It's Tuesday!")#terca
    case 'Wednesday':
        #colocar o path e o nome do arqiuvo  e indicar qual o nome do arquivo vai ter no destino
        #se for transferir um dir é necessário fazer um loop file in files:
        scp.put(localpath='C:\\Users\\pc\\Desktop\\teste\\teste.iso', remotepath= '/home/rafael/teste.iso')
        scp.close()
        ssh.close()
        print("It's Wednesday!")#quarta
    case 'Thursday':
        scp.put(localpath='C:\\Users\\pc\\Desktop\\teste\\teste.txt', remotepath= '/home/rafael/teste.txt')
        scp.close()
        ssh.close()
        print("It's Thursday!")#quinta
    case 'Friday':
        scp.put(localpath='C:\\Users\\pc\\Desktop\\teste\\teste.txt', remotepath= '/home/rafael/teste.txt')
        scp.close()
        ssh.close()
        print("It's Friday!")#sexta
    case 'Saturday':
        scp.put(localpath='C:\\Users\\pc\\Desktop\\teste\\teste.txt', remotepath= '/home/rafael/teste.txt')
        scp.close()
        ssh.close()
        print("It's Saturday!")#sabado
    case 'Sunday':
        scp.put(localpath='C:\\Users\\pc\\Desktop\\teste\\teste.txt', remotepath= '/home/rafael/teste.txt')
        scp.close()
        ssh.close()
        print("It's Sunday!")#domingo

