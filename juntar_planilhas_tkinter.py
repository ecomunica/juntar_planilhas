import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from funcoes import juntar_planilhas, juntar_unico_arquivo, move_arquivo_criado, list_directory

def selecionar_pasta_dados():
    pasta_dados = filedialog.askdirectory()
    entry_pasta_dados.delete(0, tk.END)
    entry_pasta_dados.insert(0, pasta_dados)
    print(f"Pasta de dados selecionada: {pasta_dados}")

def selecionar_pasta_juntar():
    pasta_juntar = filedialog.askdirectory()
    entry_pasta_juntar.delete(0, tk.END)
    entry_pasta_juntar.insert(0, pasta_juntar)
    print(f"Pasta de junção selecionada: {pasta_juntar}")

def iniciar_juncao():
    dir_dados = entry_pasta_dados.get()
    dir_juntar = entry_pasta_juntar.get()

    if not dir_dados or not dir_juntar:
        messagebox.showerror("Erro", "Por favor, selecione ambas as pastas.")
        return

    print(f"Diretório de dados: {dir_dados}")
    print(f"Diretório de junção: {dir_juntar}")

    # Listar todas as subpastas dentro da pasta de dados (Anos)
    directory = sorted(list_directory(dir_dados))
    total = len(directory)  # Total de pastas (anos) a serem processadas

    if total == 0:
        messagebox.showerror("Erro", "Não foram encontradas pastas na pasta de dados.")
        return

    progress_bar['maximum'] = total
    progress_bar['value'] = 0

    # Processar cada ano e atualizar a barra de progresso
    for i, ano in enumerate(directory, 1):
        print(f"Processando ano: {ano}")
        juntar_planilhas(dir_dados, ano)
        move_arquivo_criado(dir_dados, ano, dir_juntar)

        # Atualiza a barra de progresso
        progress_bar['value'] = i
        root.update_idletasks()

    # Junta todos os arquivos em um único arquivo
    juntar_unico_arquivo(dir_dados, dir_juntar)

    progress_bar['value'] = total  # Completa a barra
    messagebox.showinfo("Sucesso", "Processo de junção concluído com sucesso!")
    print("Processo de junção finalizado com sucesso.")

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Juntar Planilhas XLSX")
root.geometry("500x350")

# Seleção da pasta de dados (anos)
tk.Label(root, text="Pasta de Dados (Anos):").pack(pady=5)
entry_pasta_dados = tk.Entry(root, width=50)
entry_pasta_dados.pack(pady=5)
btn_selecionar_pasta_dados = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta_dados)
btn_selecionar_pasta_dados.pack(pady=5)

# Seleção da pasta de destino (juntar)
tk.Label(root, text="Pasta para Juntar:").pack(pady=5)
entry_pasta_juntar = tk.Entry(root, width=50)
entry_pasta_juntar.pack(pady=5)
btn_selecionar_pasta_juntar = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta_juntar)
btn_selecionar_pasta_juntar.pack(pady=5)

# Botão para iniciar o processo de junção
btn_iniciar = tk.Button(root, text="Iniciar Junção", command=iniciar_juncao)
btn_iniciar.pack(pady=20)

# Barra de Progresso
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=20)

# Inicia o loop da interface
root.mainloop()
