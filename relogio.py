import tkinter as tk
from datetime import datetime

def atualizar_relogio():
    # Obtém a hora atual
    agora = datetime.now()
    hora_atual = agora.strftime("%H:%M:%S")
    minuto = agora.strftime("%M")
    
    cor = 'white' if int(minuto) < 37 else 'red'

    # Atualiza o texto do rótulo
    label.config(text=hora_atual, fg=cor)
    
    # Agenda a próxima atualização após 1000 milissegundos (1 segundo)
    label.after(1000, atualizar_relogio)
    
# Configuração da janela principal
janela = tk.Tk()
janela.title("Relógio Python")

# Configuração do rótulo (texto)
label = tk.Label(janela, font=("Arial", 120), bg="black")
label.pack(padx=20, pady=20)

# Inicia a função
atualizar_relogio()

# Executa o loop da interface
janela.mainloop()