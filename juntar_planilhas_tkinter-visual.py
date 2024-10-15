import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import time  # Simula o tempo de execução das tarefas

# Funções simuladas para o exemplo (substituir com suas funções reais)
def selecionar_pasta_dados():
    pasta_dados = filedialog.askdirectory()
    entry_pasta_dados.delete(0, tk.END)
    entry_pasta_dados.insert(0, pasta_dados)

def selecionar_pasta_juntar():
    pasta_juntar = filedialog.askdirectory()
    entry_pasta_juntar.delete(0, tk.END)
    entry_pasta_juntar.insert(0, pasta_juntar)

def iniciar_juncao():
    dir_dados = entry_pasta_dados.get()
    dir_juntar = entry_pasta_juntar.get()

    if not dir_dados or not dir_juntar:
        messagebox.showerror("Erro", "Por favor, selecione ambas as pastas.")
        return

    # Simulação do processo com atualização da barra de progresso
    total_etapas = 10  # Simulando 10 etapas do processo
    progress_bar['maximum'] = total_etapas
    progress_bar['value'] = 0

    for etapa in range(total_etapas):
        # Simulação de trabalho - substituir por suas funções de junção
        time.sleep(0.5)  # Simula tempo de execução de cada etapa (remover no real)
        
        # Atualiza a barra de progresso
        progress_bar['value'] = etapa + 1
        root.update_idletasks()  # Atualiza a interface gráfica

    # Exibe uma mensagem de sucesso após a conclusão
    messagebox.showinfo("Sucesso", "Processo de junção concluído com sucesso!")

# Configuração da janela Tkinter
root = tk.Tk()
root.title("Juntar Planilhas XLSX")
root.geometry("500x400")

# Usando o tema do ttk (temas modernos disponíveis)
style = ttk.Style(root)
style.theme_use("clam")  # Alternativas: "clam", "alt", "default", "classic"

# Aplicando cores e estilo aos widgets
style.configure("TButton", font=('Helvetica', 10), padding=6, background="#4CAF50", foreground="white")
style.configure("TLabel", font=('Helvetica', 12))
style.configure("TEntry", padding=6)

# Frame para conter os widgets
frame = ttk.Frame(root, padding=(20, 10, 20, 10))
frame.pack(fill='x', expand=True)

# Labels e campos de entrada
ttk.Label(frame, text="Pasta que contém as pastas Anos:").pack(fill='x', pady=5)
entry_pasta_dados = ttk.Entry(frame, width=50)
entry_pasta_dados.pack(fill='x', pady=5)
btn_selecionar_pasta_dados = ttk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta_dados)
btn_selecionar_pasta_dados.pack(pady=5)

ttk.Label(frame, text="Onde você quer o arquivo junção?").pack(fill='x', pady=5)
entry_pasta_juntar = ttk.Entry(frame, width=50)
entry_pasta_juntar.pack(fill='x', pady=5)
btn_selecionar_pasta_juntar = ttk.Button(frame, text="Selecionar Pasta", command=selecionar_pasta_juntar)
btn_selecionar_pasta_juntar.pack(pady=5)

# Botão para iniciar o processo de junção
btn_iniciar = ttk.Button(frame, text="Iniciar Junção", command=iniciar_juncao)
btn_iniciar.pack(pady=20)

# Barra de Progresso
progress_bar = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=20)

# Inicia o loop da interface
root.mainloop()
