def imc_calculator(peso: float, altura: float) -> dict:
    """Essa Tool calcula o Índice de Massa Corporal (IMC) com base no peso e altura.

    Args:
        peso (float): Peso em quilogramas.
        altura (float): Altura em metros.

    Returns:
        dict: Um dicionário contendo o valor do IMC e a classificação segundo a OMS.
    """

    if altura <= 0:
        return {"erro": "Altura inválida. Por favor, informe uma altura maior que zero."}
    if peso <= 0:
        return {"erro": "Peso inválido. Por favor, informe um peso maior que zero."}
    
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        classificacao = "Peso ideal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 34.9:
        classificacao = "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III (obesidade mórbida)"

    return {
        "imc": round(imc, 2),
        "classificacao": classificacao
    }

#print(imc_calculator(68, 1.74))