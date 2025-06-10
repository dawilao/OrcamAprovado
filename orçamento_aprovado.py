import tkinter as tk
from tkinter import ttk
import re

# Função para realizar a comparação
def comparar_orcamentos():
    # Pega o texto inserido nos campos
    texto_portal = entry_portal.get("1.0", "end-1c")
    itens_input = entry_item.get("1.0", "end-1c").strip().splitlines()
    quantitativo_input = entry_quantitativo.get("1.0", "end-1c").strip().splitlines()
    
    # Processa os itens e quantitativos do ORÇAMENTO PORTAL
    items_portal = {}
    
    # Divisão do texto do orçamento portal em linhas
    linhas = texto_portal.splitlines()
    
    linhas_processadas = []
    for linha in linhas:
        linhas_processadas.append(linha)
        if "\t\t" in linha:
            linhas_processadas.append("Item excluído")
    linhas = linhas_processadas

    # Usar os índices conforme estrutura dos dados: item está na linha 1, 8, 15, etc.
    for i in range(0, len(linhas), 7):  # Para cada item, pulamos 7 linhas
        linha_item = linhas[i].strip()
        linha_quantidade = linhas[i+1].strip()
        
        # Identificar item pelo padrão (ex: 1.1, 14.6, etc.)
        match_item = re.match(r"([0-9]+\.[0-9]+|\d{1,2}\.\d{1,2})", linha_item)
        if match_item:
            item = match_item.group(1)  # Pega o código do item
            try:
                quantidade = float(linha_quantidade.replace(",", "."))
            except ValueError:
                quantidade = None  # Se não conseguir converter para float, ignora essa quantidade

            if quantidade is not None:
                items_portal[item] = quantidade

            # Verificar se a linha 7 linhas abaixo contém "Indeferido"
            if i + 6 < len(linhas):  # Verifica se existe linha 7 linhas abaixo
                status_linha = linhas[i + 6].strip()
                if "Indeferido" in status_linha:
                    items_portal[item] = "Indeferido"  # Marca como indeferido
                elif "Item excluído" in status_linha:
                    items_portal[item] = "Item excluído"

    print("Itens encontrados no ORÇAMENTO PORTAL:")
    print(items_portal)
    
    # Processa os itens e quantitativos de ITEM e QUANTITATIVO
    itens_dict = {}
    for i, item in enumerate(itens_input):
        if i < len(quantitativo_input):
            try:
                quantitativo = quantitativo_input[i].replace(",", ".")
                itens_dict[item] = float(quantitativo)
            except ValueError:
                print(f"Erro ao converter o quantitativo '{quantitativo_input[i]}' para número.")
                continue
    
    print("Itens de ITEM e QUANTITATIVO:")
    print(itens_dict)
    
    # Limpa as caixas de resultado
    entry_equivalente.delete("1.0", "end")
    entry_alteracoes.delete("1.0", "end")
    entry_adicionado.delete("1.0", "end")
    
    # Realiza a comparação e preenche as caixas de texto
    for item, quant in items_portal.items():
        if item in itens_dict:
            if itens_dict[item] == quant:
                entry_equivalente.insert("end", f"{item} tem {quant} unidades\n")
            elif quant == "Item excluído":
                entry_adicionado.insert("end", f"{item} - Item excluído\n")
            elif quant == "Indeferido":
                entry_adicionado.insert("end", f"{item} - Indeferido\n")
            else:
                diferenca = itens_dict[item] - quant
                if diferenca > 0:  # Caso em que o orçamento portal é menor
                    entry_alteracoes.insert("end", f"{item} tem {quant} unidades aprovadas no portal (no orçamento consta {diferenca:.2f} a mais)\n")
                elif diferenca < 0:  # Caso em que o orçamento portal é maior
                    entry_alteracoes.insert("end", f"{item} tem {quant} unidades aprovadas no portal (no orçamento consta {abs(diferenca):.2f} a menos)\n")
        else:
            # Verifica se o item está no orçamento portal, mas não em ITEM
            entry_adicionado.insert("end", f"{item} - Item adicionado. Consta apenas no orçamento portal\n")

    # Verifica se algum item da lista de itens fornecida não está no orçamento portal
    for item in itens_dict:
        if item not in items_portal:
            entry_adicionado.insert("end", f"{item} - Item não encontrado no orçamento portal\n")

# Cria a janela principal
janela = tk.Tk()
janela.title("Comparação de Orçamento")

# Define o tamanho da janela
janela.geometry("800x500")

# Cria um frame para organizar os widgets
frame = ttk.Frame(janela, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# 1. Título "Comparação de Orçamento" no topo, em negrito
titulo = ttk.Label(frame, text="Comparação de Orçamento", font=("Arial", 14, "bold"))
titulo.grid(row=0, column=0, columnspan=4, pady=10)

# 2. "ORÇAMENTO PORTAL" e "ORÇAMENTO REALIZADO" lado a lado
ttk.Label(frame, text="ORÇAMENTO PORTAL", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
ttk.Label(frame, text="ITEM", font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)
ttk.Label(frame, text="QUANTITATIVO", font=("Arial", 12)).grid(row=1, column=2, padx=5, pady=5)

# Caixas de texto para "ORÇAMENTO PORTAL", "ITEM" e "QUANTITATIVO"
entry_portal = tk.Text(frame, width=30, height=10)
entry_portal.grid(row=2, column=0, padx=5, pady=5)

entry_item = tk.Text(frame, width=30, height=10)
entry_item.grid(row=2, column=1, padx=5, pady=5)

entry_quantitativo = tk.Text(frame, width=30, height=10)
entry_quantitativo.grid(row=2, column=2, padx=5, pady=5)

# 3. "EQUIVALENTE", "ALTERAÇÕES" e "ADICIONADO"
ttk.Label(frame, text="EQUIVALENTE", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
ttk.Label(frame, text="ALTERAÇÕES", font=("Arial", 12)).grid(row=3, column=1, padx=5, pady=5)
ttk.Label(frame, text="ADICIONADO", font=("Arial", 12)).grid(row=3, column=2, padx=5, pady=5)

# Caixas de texto para "EQUIVALENTE", "ALTERAÇÕES" e "ADICIONADO"
entry_equivalente = tk.Text(frame, width=30, height=10)
entry_equivalente.grid(row=4, column=0, padx=5, pady=5)

entry_alteracoes = tk.Text(frame, width=30, height=10)
entry_alteracoes.grid(row=4, column=1, padx=5, pady=5)

entry_adicionado = tk.Text(frame, width=30, height=10)
entry_adicionado.grid(row=4, column=2, padx=5, pady=5)

# Botão para realizar a comparação
botao_comparar = ttk.Button(frame, text="Comparar", command=comparar_orcamentos)
botao_comparar.grid(row=5, column=0, columnspan=3, pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
