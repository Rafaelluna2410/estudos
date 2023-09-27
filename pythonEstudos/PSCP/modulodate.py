import datetime
from paramiko import SSHClient
from paramiko import SFTPClient
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='ip', port='xxxx', username='user',password='pass')
scp = ssh.open_sftp()
#colocar o path e o nome do arqiuvo  e indicar qual o nome do arquivo vai ter no destino
#se for transferir um dir é necessário fazer um loop file in files:
scp.put(localpath='C:\\xx\\pc\\xx\\xx\\teste.txt', remotepath= '/xx/xx/teste.txt')
scp.close()
ssh.close()



#day = datetime.date.today()

#name_day = day.strftime('%A')
#print(name_day)

#match name_day:
#    case 'Monday':
#        print("It's Monday!")
#    case 'Tuesday':
#        print("It's Tuesday!")
#    case 'Wednesday':
#        print("It's Wednesday!")
#    case 'Thursday':
#        print("It's Thursday!")
#    case 'Friday':
#        print("It's Friday!")
#    case 'Saturday':
#        print("It's Saturday!")
#    case 'Sunday':
#        print("It's Sunday!")

