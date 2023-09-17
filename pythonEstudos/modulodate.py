import datetime
from paramiko import SSHClient
import paramiko
from scp import SCPClient

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())
scp.put()
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

