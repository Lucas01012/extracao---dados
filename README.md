# Extração de Dados de PDF

Este projeto extrai tabelas de um arquivo PDF e converte os dados para CSV. 

## 📂 Estrutura do Projeto

```
├── data/                   # Pasta para armazenar o PDF de entrada
│   ├── Anexo1.pdf          # Arquivo PDF (deve ser colocado aqui pelo usuário)
├── scripts/                # Scripts Python para extração
│   ├── extract_pdf.py      # Script principal
│   ├── dados.csv           # Arquivo CSV gerado
│   ├── Teste_Lucas_Oliveira.zip  # Arquivo compactado
├── venv/                   # Ambiente virtual Python (opcional)
├── .gitignore              # Arquivos ignorados pelo Git
├── README.md               # Este arquivo
```

## 🚀 Como Usar

1. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

2. **Coloque o PDF na pasta `data/`**
   - O arquivo de entrada (`Anexo1.pdf`) deve ser colocado na pasta `data/` antes de rodar o script.

3. **Execute o script**
   ```bash
   cd scripts
   python extract_pdf.py
   ```

4. **Saída esperada**
   - O arquivo `dados.csv` será gerado na pasta `scripts/`
   - O arquivo compactado `Teste_Lucas_Oliveira.zip` também será gerado.

## 🛠 Tecnologias Usadas
- **Python**
- **pandas**
- **pdfplumber**
- **zipfile**
