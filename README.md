# 📊 Sistema de Comparação de Orçamentos - DAWHEN SOFTWARES

Ferramenta interna para análise e comparação automatizada de orçamentos corporativos.

## 📋 Sobre a Ferramenta

Este sistema foi desenvolvido especificamente para atender necessidades específicas, automatizando o processo de comparação entre dados de orçamentos extraídos de portais e planilhas internas de controle.

### 🎯 Objetivo

Otimizar o fluxo de trabalho da equipe na validação de orçamentos, reduzindo erros manuais e aumentando a eficiência na identificação de discrepâncias entre diferentes fontes de dados.

### ✨ Funcionalidades

- 📋 **Interface Intuitiva**: Interface gráfica moderna com tema escuro
- 🔍 **Comparação Automática**: Análise inteligente entre dados do portal e planilhas
- 📊 **Categorização de Resultados**:
  - ✅ **Equivalentes**: Itens com quantidades idênticas
  - ⚠️ **Alterações**: Itens com diferenças de quantidade
  - ➕ **Adicionados**: Itens que constam apenas em uma das fontes
- 🚫 **Detecção de Status Especiais**: Identifica itens "Indeferidos" e "Excluídos"
- 🔧 **Processamento Inteligente**: Utiliza regex para extração precisa de dados
- 📝 **Logs de Debug**: Acompanhamento detalhado no console

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **CustomTkinter** - Interface gráfica moderna
- **Re (Regex)** - Processamento de texto
- **Tkinter** - Base da interface gráfica

## 📦 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/OrcamAprovado.git
   cd OrcamAprovado
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**
   ```bash
   python orçamento_aprovado.py
   ```

## 🚀 Como Usar

1. **Dados do Portal**: Cole os dados copiados diretamente do orçamento portal no primeiro campo
2. **Itens**: Insira a lista de itens (um por linha) no segundo campo
3. **Quantitativos**: Insira as quantidades correspondentes (uma por linha) no terceiro campo
4. **Comparar**: Clique no botão "Comparar" para processar os dados
5. **Resultados**: Visualize os resultados categorizados nos campos de saída:
   - **Equivalente**: Itens com quantidades iguais
   - **Alterações**: Itens com diferenças de quantidade
   - **Adicionado**: Itens únicos ou com status especiais

### 📋 Exemplo de Uso

**Dados do Portal:**
```
1.1
100,00
Descrição do item
...
Status: Aprovado
```

**Itens:**
```
1.1
1.2
1.3
```

**Quantitativos:**
```
100,00
50,00
25,00
```

## 📁 Estrutura do Projeto

```
OrcamAprovado/
│
├── orçamento_aprovado.py    # Arquivo principal da aplicação
├── requirements.txt         # Dependências do projeto
├── README.md               # Documentação do projeto
└── LICENSE                 # Licença do projeto
```

## 🔧 Desenvolvimento

### Arquitetura

O projeto segue uma arquitetura orientada a objetos com uma única classe principal:

- **`OrcamentoAprovadoApp`**: Classe principal que encapsula toda a lógica da aplicação
  - `__init__()`: Inicialização e configuração
  - `_criar_interface()`: Criação da interface gráfica
  - `comparar_orcamentos()`: Lógica de comparação
  - `run()`: Execução da aplicação

### Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

**Dawison Nascimento**
- 📧 Email: [daw_afk@tutamail.com]
- 💼 [LinkedIn](https://www.linkedin.com/in/dawison-nascimento)
- 💻 [GitHub](https://github.com/dawilao)
- 📱 WhatsApp: +44 7979 217469

**Henrique Cardoso**
- 💼 [LinkedIn](http://www.linkedin.com/in/henrique-cardoso-3aa146331)
- 💻 [GitHub](https://github.com/Hr-CARDOSO)
- 📱 WhatsApp: +55 71 9331-0329

## 🆘 Suporte

Se você encontrar algum problema ou tiver sugestões, por favor:

1. Verifique se o problema já foi relatado nas [Issues](https://github.com/dawilao/OrcamAprovado)
2. Crie uma nova issue com detalhes do problema
3. Ou entre em contato diretamente

## 🔄 Changelog

### v0.1.0 (17/06/2025)
- 🎉 Versão inicial
- ✅ Interface gráfica completa
- ✅ Funcionalidade de comparação
- ✅ Categorização de resultados
- ✅ Documentação completa

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** ⭐
