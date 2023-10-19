import os
import shutil

caminho_origem = "C:/Users/Marcos Folharini/Downloads"
caminho_destino = "C:/Users/Marcos Folharini/Documents/teste_python"

def organizar_arquivos():
    for pasta_raiz, _, arquivos in os.walk(caminho_origem):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            extensao = arquivo.split('.')[-1]  # Obtém a extensão do arquivo
            nova_pasta = os.path.join(caminho_destino, extensao)

            if not os.path.exists(nova_pasta):
                os.makedirs(nova_pasta)

            shutil.move(caminho_completo, os.path.join(nova_pasta, arquivo))
            
organizar_arquivos()