import datetime
from paramiko import SSHClient
from paramiko import SFTPClient
import paramiko

ssh = paramiko.SSHClient()
ssh.connect(port=22, hostname="30.30.30.243", username="rafael",password="admin123")
scp = ssh.open_sftp()
scp.put(localpath="C:\\Users\\pc\\Desktop\\teste\\teste.txt", remotepath="/home/rafael")

scp.close()
ssh.close()


day = datetime.date.today()

name_day = day.strftime('%A')
print(name_day)

match name_day:
    case 'Monday':
        print("It's Monday!")
    case 'Tuesday':
        print("It's Tuesday!")
    case 'Wednesday':
        print("It's Wednesday!")
    case 'Thursday':
        print("It's Thursday!")
    case 'Friday':
        print("It's Friday!")
    case 'Saturday':
        print("It's Saturday!")
    case 'Sunday':
        print("It's Sunday!")

