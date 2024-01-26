import subprocess
import re
import time
from datetime import datetime

rota = "www.google.com.br"

limite_ms = 75

arquivo_contador = "contador_e_valores.txt"

contador = 0

flag = True
while flag:
    resultado_ping = subprocess.run(["ping", "-n", "1", rota], capture_output=True, text=True)

    if resultado_ping.returncode == 0:
        tempo_match = re.search(r"tempo[=<](\d+)", resultado_ping.stdout)
        if tempo_match:
            tempo_ping = float(tempo_match.group(1))
            if tempo_ping > limite_ms:
                contador += 1
                data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(arquivo_contador, "a") as arquivo:
                    arquivo.write(f"{data_hora_atual} - Contador: {contador}, Valor acima do limite: {tempo_ping} ms\n")
    time.sleep(1)

print(f"Contador de pings acima de {limite_ms} ms: {contador}")
