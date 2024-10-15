import os
from funcoes import *

# Diretórios
dir_path = r'/home/caminho/da/sua/pasta/juntar_planilhas/pasta_dados'
dir_junta = '/home/caminho/da/sua/pasta//juntar_planilhas/juntar'

# Listar todas as pastas de dados
directory = sorted(list_directory(dir_path))
print('Estas são as pastas:', directory)

# Processar cada pasta (Ano)
for ano in directory:
    print(f"Processando ano: {ano}")
    juntar_planilhas(dir_path, ano)
    move_arquivo_criado(dir_path, ano, dir_junta)

# Junta todos os arquivos criados em um único arquivo
juntar_unico_arquivo(dir_junta, dir_junta)

