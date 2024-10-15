import tkinter as tk

# Função simples para testar se a janela aparece
def janela_teste():
    janela = tk.Tk()
    janela.title("Janela de Teste Tkinter")
    label = tk.Label(janela, text="Tkinter está funcionando!")
    label.pack(pady=20)
    janela.geometry("300x100")
    janela.mainloop()

# Executa a função
janela_teste()
