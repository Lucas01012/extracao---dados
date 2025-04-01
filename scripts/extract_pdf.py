import pandas as pd
import pdfplumber
import zipfile
import unicodedata

pdf_caminho = "../data/Anexo1.pdf"
csv_caminho = "dados.csv"
zip_caminho = "Teste_Lucas_Oliveira.zip"

abreviacoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial",
    "HCO": "Seq. Hospitalar Com Obstetrícia",
    "HSO": "Seg. Hospitalar Sem Obstetrícia",
    "REF": "Plano Referência",
    "PAC": "Procedimento de Alta Complexidade",
    "DUT": "Diretriz de Utilização"
}

def substituir_abreviacao(valor):
    if isinstance(valor, str):
        valor = valor.strip()
        return abreviacoes.get(valor.upper(), valor)
    return valor

def normalizar_texto(texto):
    if isinstance(texto, str):
        texto = unicodedata.normalize('NFC', texto)
        texto = texto.replace("\n", " ")
        texto = " ".join(texto.split())
    return texto

def extrair_pdf_para_csv(pdf_caminho, csv_caminho):
    dados_extraidos = []
    
    try:
        with pdfplumber.open(pdf_caminho) as pdf:
            for pagina in pdf.pages:
                tabela = pagina.extract_table()

                if tabela:
                    for linha in tabela:
                        if linha and any(celula.strip() for celula in linha if celula):
                            linha_processada = [normalizar_texto(celula) if celula else "" for celula in linha]
                            linha_processada = [substituir_abreviacao(celula) for celula in linha_processada]
                            dados_extraidos.append(linha_processada)

        if dados_extraidos:
            cabecalho = dados_extraidos[0]
            dados = dados_extraidos[1:]

            colunas_max = max(len(linha) for linha in dados)
            cabecalho.extend([""] * (colunas_max - len(cabecalho)))
            dados = [linha + [""] * (colunas_max - len(linha)) for linha in dados]

            df = pd.DataFrame(dados, columns=cabecalho)
            df.to_csv(csv_caminho, sep=";", encoding="utf-8", index=False)
            return True
        else:
            print("⚠️ Nenhuma tabela encontrada no PDF.")
            return False

    except Exception as erro:
        print(f"❌ Ocorreu um erro: {erro}")
        return False

def compactar_arquivo(csv_caminho, zip_caminho):
    with zipfile.ZipFile(zip_caminho, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_caminho)

if extrair_pdf_para_csv(pdf_caminho, csv_caminho):
    compactar_arquivo(csv_caminho, zip_caminho)
    print("✅ Processo concluído com sucesso!")
else:
    print("❌ Ocorreu um erro durante o processo.")
