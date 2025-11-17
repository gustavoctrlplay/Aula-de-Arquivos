from datetime import datetime
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

def carregar_registros():
    print("Aqui vamos fazer as funções que leem as tarefas e mandam notificações :D ")


notificacoes_enviadas = set()

while True:
    agora = datetime.now().strftime("%H:%M")
    registros = carregar_registros()

    for hora, texto in registros:
        chave = f"{hora} - {texto}"

        if hora == agora and chave not in notificacoes_enviadas:
            toaster.show_toast("Lembrete", texto, duration=5, threaded=True)
            notificacoes_enviadas.add(chave)
            print("Notificação enviada:", chave)

    time.sleep(1) 
