import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def salvar():
    print("Vamos fazer aqui a nossa lista de afazeres :) ")


janela = tk.Tk() #Vai criar uma interface. Todos os códigos que usam a variável "janela" estão interagindo com a interface
janela.title("Registro de Tarefas")
janela.geometry("300x200")

tk.Label(janela, text="Horário (HH:MM):").pack() 
#tk é a biblioteca que cria a interface. 
#Label é um rótulo, ou texto simples. Entry são botões de entrada, "primos" do input 
#e Button é muito complexo para ser explicado 
entry_horario = tk.Entry(janela)
entry_horario.pack()

tk.Label(janela, text="Texto:").pack()
entry_texto = tk.Entry(janela)
entry_texto.pack()

frame_buttons = tk.Frame(janela)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Salvar", command=salvar).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Sair", command=janela.destroy).pack(side=tk.LEFT, padx=5)

janela.mainloop()
