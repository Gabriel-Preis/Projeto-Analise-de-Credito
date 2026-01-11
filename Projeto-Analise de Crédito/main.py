from entrada_dados import coletar_dados_cliente
from regras_credito import analisar_credito
from relatorio import exibir_relatorio

def main():
    print("Iniciando análise de crédito...\n")

    dados = coletar_dados_cliente()
    resultado = analisar_credito(dados)
    exibir_relatorio(dados, resultado)

if __name__ == "__main__":
    main()
