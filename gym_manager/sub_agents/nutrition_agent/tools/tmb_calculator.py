def tmb_calculator(peso: float, altura:float, idade:int, sexo: str, nivel_atividade: str) -> dict:
    """Essa Tool calcula a Taxa Metabólica Basal (TMB) com base na fórmula de Mifflin-St Jeor.

    Args:
        peso (float): Peso em quilogramas.
        altura (float): Altura em centímetros.
        idade (int): Idade em anos.
        sexo (str): 'masculino' ou 'feminino'.
        nivel_atividade (str): Nível de atividade física. Valores aceitos:
            - 'sedentario'
            - 'levemente_ativo'
            - 'moderadamente_ativo'
            - 'muito_ativo'
            - 'extremamente_ativo'

    Returns:
        dict: Um dicionário contendo a TMB, o gasto calórico diário estimado (GCD/TDEE) e mensagens explicativas.
    """
    sexo = sexo.lower()
    atividade = nivel_atividade.lower()

    fatores_atividade = {
        "sedentario": 1.2,
        "levemente_ativo": 1.375,
        "moderadamente_ativo": 1.55,
        "muito_ativo": 1.725,
        "extremamente_ativo": 1.9
    }

    if sexo not in ["masculino", "feminino"]:
        return {"erro": "Sexo inválido. Por favor, informe 'masculino' ou 'feminino'."}

    if atividade not in fatores_atividade:
        return {
            "erro": ("Nível de atividade inválido. Use: 'sedentario', 'levemente_ativo', "
                     "'moderadamente_ativo', 'muito_ativo' ou 'extremamente_ativo'.")
        }
    
    if sexo == "masculino":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    else:
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161

    # Cálculo do Gasto Total (TDEE)
    fator = fatores_atividade[atividade]
    gcd = tmb * fator

    return {
        "tmb_kcal_dia": round(tmb, 0),
        "gasto_calorico_total_kcal_dia": round(gcd, 0),
        "nivel_atividade": nivel_atividade,
        "mensagem": (
            f"Sua TMB é de aproximadamente {round(tmb,0)} kcal/dia. "
            f"Considerando o nível de atividade '{nivel_atividade}', "
            f"seu gasto calórico total estimado é de {round(gcd,0)} kcal/dia.\n"
            "Lembre-se: esses são valores estimados. Consulte um nutricionista para um plano personalizado."
        )
    }


#print(tmb_calculator(peso=68.0, altura=174, idade=24, sexo='masculino', nivel_atividade='moderadamente_ativo'))