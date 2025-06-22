def creatine_calculator(peso: float, medidor: float = 3.0) -> dict:
    """Essa Tool calcula a quantidade diária recomendada de creatina com base no peso corporal.

    Args:
        peso (float): Peso em quilogramas.
        medidor (float, opcional): Quantidade de creatina (em gramas) presente em um medidor. Padrão: 3.0g.

    Returns:
        dict: Um dicionário contendo a quantidade recomendada de creatina em gramas e a equivalência aproximada em número de medidores.
    """
    if peso <= 0 or medidor <= 0:
        return {"erro": "Peso e tamanho do medidor devem ser maiores que zero."}

    amount = peso * 0.06
    scoops = amount / medidor

    return {
        "quantidade_gramas": round(amount, 2),
        "quantidade_medidores": round(scoops, 2),
        "medidor_em_gramas": medidor,
        "mensagem": (
            f"A quantidade de creatina ideal para seu peso é de {amount:.2f} gramas.\n"
            f"Isso equivale a {scoops:.2f} medidor de {medidor}"
        )
    }

#print(creatine_calculator(68))
