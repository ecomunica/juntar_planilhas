import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import filedialog, messagebox
import time

# Funções para selecionar pastas
def selecionar_pasta_dados():
    pasta_dados = filedialog.askdirectory()
    entry_pasta_dados.delete(0, tk.END)
    entry_pasta_dados.insert(0, pasta_dados)

def selecionar_pasta_juntar():
    pasta_juntar = filedialog.askdirectory()
    entry_pasta_juntar.delete(0, tk.END)
    entry_pasta_juntar.insert(0, pasta_juntar)

# Função de junção (simulação) com barra de progresso indeterminada
def iniciar_juncao_indeterminada():
    dir_dados = entry_pasta_dados.get()
    dir_juntar = entry_pasta_juntar.get()

    if not dir_dados or not dir_juntar:
        messagebox.showerror("Erro", "Por favor, selecione ambas as pastas.")
        return

    # Inicia a barra de progresso indeterminada
    progress_bar.config(mode='indeterminate')
    progress_bar.start(10)  # Velocidade de rotação

    root.update_idletasks()  # Garante que a interface continue responsiva

    # Simulando um processo (substitua pela sua lógica real)
    for _ in range(10):  # Simule um processo que demora 10 segundos
        time.sleep(1)  # Simule o tempo de execução de uma etapa
        root.update_idletasks()

    # Para a barra de progresso quando terminar
    progress_bar.stop()
    messagebox.showinfo("Sucesso", "Processo de junção concluído com sucesso!")

# Configuração da janela principal com ttkbootstrap
root = ttk.Window(themename="cosmo")  # Você pode escolher outro tema: "darkly", "flatly", "cosmo", "cyborg", "journal".
root.title("Juntar Planilhas XLSX")
root.geometry("600x400")

# Frame principal para contenção dos widgets
frame = ttk.Frame(root, padding=(20, 10, 20, 10))
frame.grid(row=0, column=0, sticky="nsew")

# Configuração de responsividade
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame.grid_propagate(False)  # Desativa propagação automática do grid

# Labels e campos de entrada com ttkbootstrap
ttk.Label(frame, text="Pasta que contém as pastas Anos:", bootstyle="info").grid(row=0, column=0, sticky="w", pady=5)
entry_pasta_dados = ttk.Entry(frame, width=50)
entry_pasta_dados.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

btn_selecionar_pasta_dados = ttk.Button(frame, text="Selecionar Pasta", bootstyle="primary", command=selecionar_pasta_dados)
btn_selecionar_pasta_dados.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

ttk.Label(frame, text="Onde você quer o arquivo junção?", bootstyle="info").grid(row=3, column=0, sticky="w", pady=5)
entry_pasta_juntar = ttk.Entry(frame, width=50)
entry_pasta_juntar.grid(row=4, column=0, sticky="ew", padx=10, pady=5)

btn_selecionar_pasta_juntar = ttk.Button(frame, text="Selecionar Pasta", bootstyle="primary", command=selecionar_pasta_juntar)
btn_selecionar_pasta_juntar.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

# Botão para iniciar o processo de junção
btn_iniciar = ttk.Button(frame, text="Iniciar Junção", bootstyle="success", command=iniciar_juncao_indeterminada)
btn_iniciar.grid(row=6, column=0, sticky="ew", padx=10, pady=20)

# Barra de Progresso indeterminada com estilo
progress_bar = ttk.Progressbar(frame, bootstyle="info-striped", orient="horizontal", length=400, mode="indeterminate")
progress_bar.grid(row=7, column=0, sticky="ew", padx=10, pady=20)

# Responsividade
root.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Inicia o loop da interface gráfica
root.mainloop()
