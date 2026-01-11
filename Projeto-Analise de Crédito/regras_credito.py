def analisar_credito(cliente):
    score = 0

    if cliente["idade"] >= 18:
        score += 1
    if cliente["renda"] >= 2000:
        score += 1
    if cliente["empregado"]:
        score += 1
    if score >= 2:
        return "Crédito aprovado"
    else:
        return "Crédito negado"
    
   
