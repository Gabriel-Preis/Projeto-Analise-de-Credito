def coletar_dados_cliente():
    nome = input("Nome do Cliente: ")
    idade = int(input("Idade: "))
    renda = float(input("renda mensal: "))
    resposta = input("Está empregado? (sim/não)").lower()
    
    if resposta == "sim":
        empregado = True
    elif resposta == "não" or resposta == "nao":
        empregado = False
    else:
        empregado = False

    cliente = {
        "nome": nome,
        "idade": idade,
        "renda": renda,
        "empregado": empregado
    }

    return cliente
