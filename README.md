Como usar
Selecione a pasta de dados: Esta é a pasta que contém subpastas com arquivos Excel por ano/mês, que você deseja combinar.

Selecione a pasta de destino: Esta é a pasta onde os arquivos combinados serão salvos.

Iniciar junção: Clique em "Iniciar Junção" para começar o processo. Uma barra de progresso mostrará o andamento da tarefa.

Funcionalidades
Junção de planilhas por ano: O script percorre cada pasta de ano, junta os arquivos Excel encontrados e salva um arquivo por ano.
Junção final: Após processar todos os anos, o script junta todos os arquivos em um único arquivo final chamado juntar_final.xlsx.
Problemas comuns
Tkinter não abre: Se a janela não aparecer ao executar o script, verifique se o Tkinter está corretamente instalado. Siga as instruções de instalação no início deste documento para instalar o Tkinter.
Erro de biblioteca: Se você encontrar um erro dizendo que a biblioteca pandas ou openpyxl não foi encontrada, verifique se o comando pip install -r requirements.txt foi executado corretamente.



Estrutura do Projeto
A estrutura do projeto deve se parecer com isso:

juntar_planilhas_aprimorado/
│
├── juntar_planilhas_tkinter.py   # Script principal com Tkinter
├── funcoes.py                    # Funções auxiliares para juntar planilhas
├── requirements.txt              # Dependências do projeto
├── HOW_TO.md                     # Instruções de uso (este arquivo)
└── README.md                     # Descrição do projeto

Requisitos para as pastas de dados
A pasta de dados deve conter subpastas organizadas por ano (por exemplo, 2022, 2023).
Cada subpasta deve conter arquivos .xlsx para cada mês que você deseja juntar.
Exemplo de estrutura de pastas:
pasta_dados/
├── 2022/
│   ├── janeiro.xlsx
│   ├── fevereiro.xlsx
│   └── ...
├── 2023/
│   ├── janeiro.xlsx
│   ├── fevereiro.xlsx
│   └── ...
└── ...
O script lerá e processará essas pastas automaticamente.

# Como instalar e usar o script de junção de planilhas Excel

Este documento descreve como instalar e executar o script de junção de arquivos `.xlsx` usando uma interface gráfica feita em **Tkinter**. 
A aplicação permite selecionar pastas contendo arquivos Excel e combiná-los em um único arquivo.

## Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes componentes instalados:

1. **Python 3.6 ou superior** - [Instalar Python](https://www.python.org/downloads/)
2. **Bibliotecas necessárias** (listadas abaixo) - que serão instaladas automaticamente com `pip`.

### Bibliotecas Python necessárias

As seguintes bibliotecas Python são necessárias:

- `pandas`
- `openpyxl`
- `tkinter` (nativo na maioria das instalações Python)

## Instalação

### 1. Clone ou baixe o repositório do projeto

Você pode baixar este projeto ou cloná-lo via Git:

```bash
https://github.com/ecomunica/juntar_planilhas.git


