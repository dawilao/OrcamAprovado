import customtkinter as ctk
import re

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Função para realizar a comparação
def comparar_orcamentos():
    texto_portal = entry_portal.get("1.0", "end-1c")
    itens_input = entry_item.get("1.0", "end-1c").strip().splitlines()
    quantitativo_input = entry_quantitativo.get("1.0", "end-1c").strip().splitlines()

    items_portal = {}
    linhas = [linha for linha in texto_portal.splitlines() if not linha.startswith("Total dos Itens")]

    linhas_processadas = []
    for linha in linhas:
        linhas_processadas.append(linha)
        if "\t\t" in linha:
            linhas_processadas.append("Item excluído")
    linhas = linhas_processadas

    for i in range(0, len(linhas), 7):
        linha_item = linhas[i].strip()
        linha_quantidade = linhas[i+1].strip()

        match_item = re.match(r"([0-9]+\.[0-9]+|\d{1,2}\.\d{1,2})", linha_item)
        if match_item:
            item = match_item.group(1)
            try:
                quantidade = float(linha_quantidade.replace(",", "."))
            except ValueError:
                quantidade = None

            if quantidade is not None:
                items_portal[item] = quantidade

            if i + 6 < len(linhas):
                status_linha = linhas[i + 6].strip()
                if "Indeferido" in status_linha:
                    items_portal[item] = "Indeferido"
                elif "Item excluído" in status_linha:
                    items_portal[item] = "Item excluído"

    print("Itens encontrados no ORÇAMENTO PORTAL:")
    print(items_portal)

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

    entry_equivalente.delete("1.0", "end")
    entry_alteracoes.delete("1.0", "end")
    entry_adicionado.delete("1.0", "end")

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
                if diferenca > 0:
                    entry_alteracoes.insert("end", f"{item} tem {quant} unidades aprovadas no portal (no orçamento consta {diferenca:.2f} a mais)\n")
                elif diferenca < 0:
                    entry_alteracoes.insert("end", f"{item} tem {quant} unidades aprovadas no portal (no orçamento consta {abs(diferenca):.2f} a menos)\n")
        else:
            entry_adicionado.insert("end", f"{item} - Item adicionado. Consta apenas no orçamento portal\n")

    for item in itens_dict:
        if item not in items_portal:
            entry_adicionado.insert("end", f"{item} - Item não encontrado no orçamento portal\n")

# Cria a janela principal
janela = ctk.CTk()
janela.title("Comparação de Orçamento")
janela.geometry("800x600")

frame = ctk.CTkFrame(janela)
frame.pack(fill="both", expand=True, padx=10, pady=10)

titulo = ctk.CTkLabel(frame, text="Comparação de Orçamento", font=("Arial", 16, "bold"))
titulo.grid(row=0, column=0, columnspan=4, pady=10)

ctk.CTkLabel(frame, text="ORÇAMENTO PORTAL", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
ctk.CTkLabel(frame, text="ITEM", font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)
ctk.CTkLabel(frame, text="QUANTITATIVO", font=("Arial", 12)).grid(row=1, column=2, padx=5, pady=5)

entry_portal = ctk.CTkTextbox(frame, width=240, height=160)
entry_portal.grid(row=2, column=0, padx=5, pady=5)

entry_item = ctk.CTkTextbox(frame, width=240, height=160)
entry_item.grid(row=2, column=1, padx=5, pady=5)

entry_quantitativo = ctk.CTkTextbox(frame, width=240, height=160)
entry_quantitativo.grid(row=2, column=2, padx=5, pady=5)

ctk.CTkLabel(frame, text="EQUIVALENTE", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
ctk.CTkLabel(frame, text="ALTERAÇÕES", font=("Arial", 12)).grid(row=3, column=1, padx=5, pady=5)
ctk.CTkLabel(frame, text="ADICIONADO", font=("Arial", 12)).grid(row=3, column=2, padx=5, pady=5)

entry_equivalente = ctk.CTkTextbox(frame, width=240, height=160)
entry_equivalente.grid(row=4, column=0, padx=5, pady=5)

entry_alteracoes = ctk.CTkTextbox(frame, width=240, height=160)
entry_alteracoes.grid(row=4, column=1, padx=5, pady=5)

entry_adicionado = ctk.CTkTextbox(frame, width=240, height=160)
entry_adicionado.grid(row=4, column=2, padx=5, pady=5)

botao_comparar = ctk.CTkButton(frame, text="Comparar", command=comparar_orcamentos)
botao_comparar.grid(row=5, column=0, columnspan=3, pady=20)

janela.mainloop()
