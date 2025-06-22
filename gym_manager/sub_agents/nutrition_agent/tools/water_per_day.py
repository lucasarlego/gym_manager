def water_per_day(peso: float) -> dict:
    """Essa Tool calcula a quantidade recomendada de água por dia com base no peso corporal.

    Args:
        peso (float): Peso em quilogramas.

    Returns:
        dict: Um dicionário contendo a quantidade recomendada de água em mililitros e litros.
    """
    if peso <= 0:
        return {"erro": "Peso inválido. Por favor, informe um peso maior que zero."}
    
    quantidade_ml = peso * 35
    quantidade_litros = quantidade_ml / 1000

    return {
        "quantidade_ml": round(quantidade_ml, 0),
        "quantidade_litros": round(quantidade_litros, 2),
        "recomendacao": f"A recomendação geral é consumir aproximadamente {quantidade_litros:.2f} litros de água por dia."
    }

#print(water_per_day(68))