import os

directory = "C:\\Users\\caio6\\OneDrive\\Área de Trabalho\\Cursos\\sistema_gerenciador"
arquivos = [arq for arq in os.listdir(directory) if arq.endswith(".xml")]

print("Arquivos encontrados:", arquivos)
