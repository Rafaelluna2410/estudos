from paramiko import SSHClient
from scp import SCPClient
import pysftp


ssh = SSHClient()
ssh.load_host_keys
ssh.connect()
ssh.exec_command()