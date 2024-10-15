import os
import pandas as pd
from pathlib import Path
import shutil

def list_files(dir_path):
    """Listar todos os arquivos em um diretório."""
    try:
        return [file for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file))]
    except Exception as e:
        print(f"Erro ao listar arquivos em {dir_path}: {e}")
        return []

def list_directory(dir_path):
    """Listar todas as subpastas dentro de um diretório."""
    try:
        return [folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))]
    except Exception as e:
        print(f"Erro ao listar pastas em {dir_path}: {e}")
        return []

def juntar_planilhas(dir_path, ano):
    """Junta todas as planilhas de uma pasta por ano e salva em um único arquivo."""
    data_arquivo_folder = os.path.join(dir_path, ano)
    df_list = []

    for file in sorted(os.listdir(data_arquivo_folder)):  # Ordenar arquivos por mês
        if file.endswith('.xlsx'):
            print(f"{ano} - Carregando arquivo: {file}")
            df = pd.read_excel(os.path.join(data_arquivo_folder, file))
            df['Mes'] = os.path.splitext(file)[0]
            df['Ano'] = ano
            df_list.append(df)

    # Concatena todas as planilhas e salva em um único arquivo por ano
    df_principal = pd.concat(df_list, axis=0)
    nome_arquivo = os.path.join(data_arquivo_folder, f'juntar_{ano}.xlsx')
    df_principal.to_excel(nome_arquivo, index=False)
    print(f"Arquivo salvo: {nome_arquivo}")

def move_arquivo_criado(dir_path, ano, dir_junta):
    """Move o arquivo criado para a pasta de junção."""
    nome_dir_path = os.path.join(dir_path, ano)
    for file in os.listdir(nome_dir_path):
        if file.startswith('juntar'):
            source = os.path.join(nome_dir_path, file)
            destination = os.path.join(dir_junta, file)
            shutil.move(source, destination)
            print(f"Movido: {source} -> {destination}")

def juntar_unico_arquivo(dir_path, dir_junta):
    """Junta todos os arquivos 'juntar_Ano.xlsx' em um único arquivo."""
    df_list = []

    for file in sorted(os.listdir(dir_junta)):
        if file.endswith('.xlsx'):
            print(f"Carregando arquivo {file}...")
            df = pd.read_excel(os.path.join(dir_junta, file))
            df_list.append(df)

    df_principal = pd.concat(df_list, axis=0)
    nome_arquivo = os.path.join(dir_junta, 'juntar_final.xlsx')
    df_principal.to_excel(nome_arquivo, index=False)
    print(f"Arquivo final salvo: {nome_arquivo}")
