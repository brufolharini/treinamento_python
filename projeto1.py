import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Função para mover arquivos
def organizar_arquivos(origem, destino):
    for root, dirs, files in os.walk(origem):
        for file in files:
            src_path = os.path.join(root, file)
            file_extension = file.split(".")[-1]
            dst_path = os.path.join(destino, file_extension)
            
            # Cria a pasta de destino se não existir
            os.makedirs(dst_path, exist_ok=True)
            
            # Move o arquivo para a pasta de destino
            shutil.move(src_path, os.path.join(dst_path, file))

# Função para escolher a pasta de origem
def escolher_origem():
    global pasta_origem
    pasta_origem = filedialog.askdirectory()
    origem_label.config(text="Pasta de Origem: " + pasta_origem)

# Função para escolher a pasta de destino
def escolher_destino():
    global pasta_destino
    pasta_destino = filedialog.askdirectory()
    destino_label.config(text="Pasta de Destino: " + pasta_destino)

# Função para organizar os arquivos
def organizar():
    if not pasta_origem or not pasta_destino:
        resultado_label.config(text="Selecione a pasta de origem e a pasta de destino.")
        return
    
    organizar_arquivos(pasta_origem, pasta_destino)
    resultado_label.config(text="Arquivos organizados com sucesso.")

# Configuração da janela principal
root = tk.Tk()
root.title("Organizador de Arquivos")

# Labels
origem_label = tk.Label(root, text="Pasta de Origem: ")
origem_label.pack()

destino_label = tk.Label(root, text="Pasta de Destino: ")
destino_label.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Botões
origem_button = tk.Button(root, text="Escolher Origem", command=escolher_origem)
origem_button.pack()

destino_button = tk.Button(root, text="Escolher Destino", command=escolher_destino)
destino_button.pack()

organizar_button = tk.Button(root, text="Organizar Arquivos", command=organizar)
organizar_button.pack()

root.mainloop()