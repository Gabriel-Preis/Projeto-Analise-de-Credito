def exibir_relatorio(cliente, resultado_credito):
    print("\n---RELATORIO DE ÁNALISE DE CRÉDITO---")
    print(f"nome: {cliente['nome']}")
    print(f"idade: {cliente['idade']} anos" )
    print(f"renda mensal: R$ {cliente['renda']:.2f}")
    print(f"empregado: {cliente['empregado']}")
    print("------------------------------------------")
    print(f"Resultado: {resultado_credito}")