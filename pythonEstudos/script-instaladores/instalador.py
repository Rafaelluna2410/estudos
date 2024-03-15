import subprocess as tarefa
from pathlib import Path
import os 

home_dir = str(Path.home())
site = "https://download.anydesk.com/AnyDesk.exe"
executar = "AnyDesk.exe"
download = f"powershell.exe -Command \"Invoke-WebRequest -Uri '{site}' -OutFile '{executar}'\""


instalador = ".\\Anydesk.exe --install"
path_install = r"C:\Program Files (x86)\AnyDesk --start-with-win --create-desktop-icon"
instalar_anydesk = f"{instalador} {path_install}"
senha =""
passsword= f"echo {senha} | .\\Anydesk.exe --set-password"

os.chdir(home_dir)

#try:
#    os.chdir("Downloads")
#except FileNotFoundError:
#    print("Diretório Downloads não encontrado")
#    os.chdir(home_dir)
os.chdir(os.path.join(home_dir, "Downloads"))
#tarefa.run(download, shell=True)
tarefa.run(instalar_anydesk, shell=True)

os.chdir(r"C:\Program Files (x86)\AnyDesk")
tarefa.run(".\Anydesk", "--stop-service	")
tarefa.run(passsword, shell=True)
print(os.getcwd())
