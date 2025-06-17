"""
Aplicação de Comparação de Orçamentos Aprovados

Este módulo contém uma aplicação GUI desenvolvida com CustomTkinter para comparar
orçamentos entre dados extraídos de um portal e planilhas de itens/quantitativos.

A aplicação permite:
- Inserir dados de orçamento copiados diretamente do portal
- Inserir listas de itens e seus respectivos quantitativos
- Realizar comparação automática entre os dados
- Categorizar resultados em: equivalentes, alterações e itens adicionados
- Identificar status especiais como "Indeferido" e "Item excluído"

Funcionalidades principais:
- Interface gráfica intuitiva com tema escuro
- Processamento de texto com regex para extração de dados
- Validação e conversão de dados numéricos
- Exibição categorizada dos resultados da comparação
- Logs de debug no console para acompanhamento

Autor: DAWHEN SOFTWARES
Data: 17 de junho de 2025
Versão: 0.1.0

Dependências:
- customtkinter: Para interface gráfica moderna
- re: Para processamento de texto com expressões regulares
"""

import customtkinter as ctk
import re

class OrcamentoAprovadoApp:
    """
    Aplicação para comparação de orçamentos entre portal e planilha.
    
    Esta classe cria uma interface gráfica que permite ao usuário inserir dados
    de orçamento do portal e de itens/quantitativos, realizando a comparação
    e exibindo os resultados categorizados em equivalentes, alterações e adicionados.
    """
    
    def __init__(self):
        """
        Inicializa a aplicação de comparação de orçamentos.
        
        Configura o tema da interface, cria a janela principal e
        inicializa todos os componentes da interface gráfica.
        """
        # Configuração do tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Cria a janela principal
        self.janela = ctk.CTk()
        self.janela.title("Comparação de Orçamento")
        self.janela.geometry("800x600")
        
        self._criar_interface()        
    def _criar_interface(self):
        """
        Cria e configura todos os elementos da interface gráfica.
        
        Este método privado é responsável por:
        - Criar o frame principal
        - Adicionar labels e textboxes para entrada de dados
        - Configurar o layout em grid
        - Criar o botão de comparação
        """
        frame = ctk.CTkFrame(self.janela)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        titulo = ctk.CTkLabel(frame, text="Comparação de Orçamento", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=4, pady=10)
        
        ctk.CTkLabel(frame, text="ORÇAMENTO PORTAL", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkLabel(frame, text="ITEM", font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)
        ctk.CTkLabel(frame, text="QUANTITATIVO", font=("Arial", 12)).grid(row=1, column=2, padx=5, pady=5)
        
        self.entry_portal = ctk.CTkTextbox(frame, width=240, height=160)
        self.entry_portal.grid(row=2, column=0, padx=5, pady=5)
        
        self.entry_item = ctk.CTkTextbox(frame, width=240, height=160)
        self.entry_item.grid(row=2, column=1, padx=5, pady=5)
        
        self.entry_quantitativo = ctk.CTkTextbox(frame, width=240, height=160)
        self.entry_quantitativo.grid(row=2, column=2, padx=5, pady=5)
        
        ctk.CTkLabel(frame, text="EQUIVALENTE", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
        ctk.CTkLabel(frame, text="ALTERAÇÕES", font=("Arial", 12)).grid(row=3, column=1, padx=5, pady=5)
        ctk.CTkLabel(frame, text="ADICIONADO", font=("Arial", 12)).grid(row=3, column=2, padx=5, pady=5)
        
        self.entry_equivalente = ctk.CTkTextbox(frame, width=240, height=160)
        self.entry_equivalente.grid(row=4, column=0, padx=5, pady=5)
        
        self.entry_alteracoes = ctk.CTkTextbox(frame, width=240, height=160)
        self.entry_alteracoes.grid(row=4, column=1, padx=5, pady=5)
        
        self.entry_adicionado = ctk.CTkTextbox(frame, width=240, height=160)
        self.entry_adicionado.grid(row=4, column=2, padx=5, pady=5)
        
        botao_comparar = ctk.CTkButton(frame, text="Comparar", command=self.comparar_orcamentos)
        botao_comparar.grid(row=5, column=0, columnspan=3, pady=20)    
    def comparar_orcamentos(self):
        """
        Realiza a comparação entre os dados do orçamento portal e os itens/quantitativos.
        
        Este método:
        1. Extrai os dados dos campos de entrada
        2. Processa o texto do orçamento portal para identificar itens e quantidades
        3. Identifica status especiais (Indeferido, Item excluído)
        4. Compara com os dados de itens e quantitativos fornecidos
        5. Categoriza os resultados em: equivalentes, alterações e adicionados
        6. Atualiza os campos de saída com os resultados da comparação
        
        Exibe também informações de debug no console para acompanhamento.
        """
        texto_portal = self.entry_portal.get("1.0", "end-1c")
        itens_input = self.entry_item.get("1.0", "end-1c").strip().splitlines()
        quantitativo_input = self.entry_quantitativo.get("1.0", "end-1c").strip().splitlines()

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

        self.entry_equivalente.delete("1.0", "end")
        self.entry_alteracoes.delete("1.0", "end")
        self.entry_adicionado.delete("1.0", "end")

        for item, quant in items_portal.items():
            if item in itens_dict:
                if itens_dict[item] == quant:
                    self.entry_equivalente.insert("end", f"{item} tem {quant} unidades\n")
                elif quant == "Item excluído":
                    self.entry_adicionado.insert("end", f"{item} - Item excluído\n")
                elif quant == "Indeferido":
                    self.entry_adicionado.insert("end", f"{item} - Indeferido\n")
                else:
                    diferenca = itens_dict[item] - quant
                    if diferenca > 0:
                        self.entry_alteracoes.insert("end", f"{item} tem {quant} unidades aprovadas no portal (no orçamento consta {diferenca:.2f} a mais)\n")
                    elif diferenca < 0:
                        self.entry_alteracoes.insert("end", f"{item} tem {quant} unidades aprovadas no portal (no orçamento consta {abs(diferenca):.2f} a menos)\n")
            else:
                self.entry_adicionado.insert("end", f"{item} - Item adicionado. Consta apenas no orçamento portal\n")

        for item in itens_dict:
            if item not in items_portal:
                self.entry_adicionado.insert("end", f"{item} - Item não encontrado no orçamento portal\n")
    def run(self):
        """
        Inicia a execução da aplicação.
        
        Este método inicia o loop principal da interface gráfica,
        mantendo a aplicação em execução até que o usuário feche a janela.
        """
        self.janela.mainloop()

if __name__ == "__main__":
    app = OrcamentoAprovadoApp()
    app.run()
