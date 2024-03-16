import os
import subprocess
from pathlib import Path
import psutil


# Procura o anydesk na tabela de processos do windows 
def find_anydesk(nome_processo='Anydesk'):
    for processo in psutil.process_iter():
        try:
            if nome_processo.lower() in processo.name().lower():
                return processo
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None

# Verifica se há anydesk na máquina 
def find_anydesk_local_machine():
    s = psutil.win_service_get('Anydesk')
    return s

# Anydesk estiver online ele redefine a senha
#if status_anydesk() == 'online':
#    try:
#        os.chdir(r"C:\Program Files (x86)\AnyDesk")
#        result = subprocess.run(['Anydesk.exe', '--set-password'], input='rafael123\n', check=True, capture_output=True, text=True)
#    except subprocess.CalledProcessError as e:
#        print("Erro ao definir a senha do AnyDesk:", e)
#        print("Standard error output:", e.stderr)
 

def install_full():
    home_dir = str(Path.home())
    site = "https://download.anydesk.com/AnyDesk.exe"
    executar = "AnyDesk.exe"
    download = f"powershell.exe -Command \"Invoke-WebRequest -Uri '{site}' -OutFile '{executar}'\""
    os.chdir(home_dir)
    try:
        subprocess.run(download, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Erro ao baixar AnyDesk:", e)
    try:
        subprocess.run(['Anydesk.exe', '--install', r'C:\Program Files (x86)\AnyDesk', '--start-with-win', '--create-desktop-icon'], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Erro ao instalar AnyDesk:", e)
    try:
        os.chdir(r"C:\Program Files (x86)\AnyDesk")
        result = subprocess.run(['Anydesk.exe', '--set-password'], input='senha123\n', check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print("Erro ao definir a senha do AnyDesk:", e)
        print("Standard error output:", e.stderr)
    else:
        print("Password set successfully:", result.stdout)
    print("Instalação e configuração do AnyDesk concluídas.") 

# busca se há o anydesk e dependendo instala
try:
    find_anydesk_local_machine()
    if find_anydesk():
        print("Anydesk já está instalado e aberto")
except psutil.NoSuchProcess:
    install_full()
