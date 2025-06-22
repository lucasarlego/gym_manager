def protein_calculator(
    peso: float,
    idade: int,
    nivel_atividade: str,
    objetivo: str,
    tipo_exercicio: str,
    saude_geral: str
) -> dict:
    """Essa Tool calcula a quantidade diária recomendada de proteína com base em fatores individuais.

    Args:
        peso (float): Peso corporal em quilogramas.
        idade (int): Idade em anos.
        nivel_atividade (str): Nível de atividade física. Valores aceitos:
            - 'sedentario' (pouco ou nenhum exercício)
            - 'moderadamente_ativo' (atividade física moderada algumas vezes por semana)
            - 'altamente_ativo' (atividade física intensa na maioria dos dias)
        objetivo (str): Objetivo do usuário em relação ao treino. Valores aceitos:
            - 'perda_de_peso'
            - 'ganho_de_massa'
            - 'manutencao'
        tipo_exercicio (str): Tipo predominante de atividade física realizada. Valores aceitos:
            - 'nenhum'
            - 'musculacao'
            - 'resistencia' (ex: corrida, ciclismo, esportes de endurance)
        saude_geral (str): Condição geral de saúde. Valores aceitos:
            - 'normal'
            - 'condicao_especial' (ex: condições médicas que requerem ajustes nutricionais)

    Returns:
        str: Texto contendo a faixa estimada de proteína recomendada por dia (em gramas), com explicação sobre os critérios usados.
    """
    atividade_fatores = {
        "sedentario": (0.8, 1.0),
        "moderadamente_ativo": (1.2, 1.6),
        "altamente_ativo": (1.6, 2.2)
    }

    # Validações
    if nivel_atividade not in atividade_fatores:
        return {"erro": "Nível de atividade inválido. Valores aceitos: 'sedentario', 'moderadamente_ativo', 'altamente_ativo'."}

    if objetivo not in ["perda_de_peso", "ganho_de_massa", "manutencao"]:
        return {"erro": "Objetivo inválido. Valores aceitos: 'perda_de_peso', 'ganho_de_massa', 'manutencao'."}

    if tipo_exercicio not in ["nenhum", "musculacao", "resistencia"]:
        return {"erro": "Tipo de exercício inválido. Valores aceitos: 'nenhum', 'musculacao', 'resistencia'."}

    if saude_geral not in ["normal", "condicao_especial"]:
        return {"erro": "Saúde geral inválida. Valores aceitos: 'normal', 'condicao_especial'."}

    faixa_min, faixa_max = atividade_fatores[nivel_atividade]

    # Ajustes conforme o objetivo
    if objetivo == "ganho_de_massa":
        faixa_min *= 1.1
        faixa_max *= 1.2
    elif objetivo == "perda_de_peso":
        faixa_min = faixa_max  # Inclina para o topo da faixa para preservar massa magra

    # Ajustes conforme o tipo de exercício
    if tipo_exercicio == "musculacao":
        faixa_min += 0.1
        faixa_max += 0.2
    elif tipo_exercicio == "resistencia":
        faixa_min += 0.05
        faixa_max += 0.1

    # Cálculo final
    proteina_min = peso * faixa_min
    proteina_max = peso * faixa_max

    # Monta a resposta
    mensagem = (
        f"Recomenda-se uma ingestão diária de proteína entre {proteina_min:.1f}g e {proteina_max:.1f}g "
        f"com base nas suas informações (peso: {peso}kg, nível de atividade: {nivel_atividade}, "
        f"objetivo: {objetivo}, tipo de exercício: {tipo_exercicio})."
    )

    if saude_geral == "condicao_especial":
        mensagem += " Atenção: Como você indicou uma condição especial de saúde, consulte um nutricionista antes de seguir esta recomendação."

    return {
        "proteina_minima_g": round(proteina_min, 1),
        "proteina_maxima_g": round(proteina_max, 1),
        "nivel_atividade": nivel_atividade,
        "objetivo": objetivo,
        "tipo_exercicio": tipo_exercicio,
        "saude_geral": saude_geral,
        "mensagem": mensagem
    }


#print(protein_calculator(
#    peso=68,
#    idade=24,
#    nivel_atividade="moderadamente_ativo",
#    objetivo="ganho_de_massa",
#    tipo_exercicio="musculacao",
#    saude_geral="normal"
#))