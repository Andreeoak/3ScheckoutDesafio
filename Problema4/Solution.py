'''
Escreva uma função que calcula o quanto um funcionário tem a receber de dois benefícios: Férias e Décimo Terceiro Salário ao pedir demissão.

Simplificando o cenário, as férias zeram a cada aniversário de emprego (ou seja, ele sempre tirou as férias corretamente) 
e o décimo terceiro zera a cada virada de ano (não fica nenhum valor residual de um ano para outro).

'''

def calcular_beneficios(salario_mensal: float, meses_trabalhados_no_ano: int, meses_desde_ultimo_aniversario: int) -> dict:
    """
    Calcula Férias proporcionais e Décimo Terceiro ao pedir demissão.

    Args:
        salario_mensal: salário mensal do funcionário
        meses_trabalhados_no_ano: meses trabalhados no ano corrente (1-12)
        meses_desde_ultimo_aniversario: meses trabalhados desde o último aniversário de emprego (0-12)

    Returns:
        dict com os valores de férias e décimo terceiro proporcionais
    """
    if not (0 <= meses_trabalhados_no_ano <= 12):
        raise ValueError("meses_trabalhados_no_ano deve estar entre 0 e 12")
    if not (0 <= meses_desde_ultimo_aniversario <= 12):
        raise ValueError("meses_desde_ultimo_aniversario deve estar entre 0 e 12")
    if salario_mensal < 0:
        raise ValueError("salario_mensal deve ser positivo")

    # Férias proporcionais
    ferias = salario_mensal * (meses_desde_ultimo_aniversario / 12)

    # Décimo terceiro proporcional
    decimo_terceiro = salario_mensal * (meses_trabalhados_no_ano / 12)

    return {
        "ferias": round(ferias, 2),
        "decimo_terceiro": round(decimo_terceiro, 2)
    }

def main():
    try:
        salario_mensal = float(input("Digite o salário mensal: R$ "))
        meses_trabalhados_no_ano = int(input("Digite os meses trabalhados no ano corrente (0-12): "))
        meses_desde_ultimo_aniversario = int(input("Digite os meses desde o último aniversário de emprego (0-12): "))

        beneficios = calcular_beneficios(
            salario_mensal, 
            meses_trabalhados_no_ano, 
            meses_desde_ultimo_aniversario
        )

        print(f"\nFérias proporcionais: R${beneficios['ferias']}")
        print(f"Décimo terceiro proporcional: R${beneficios['decimo_terceiro']}")

    except ValueError as e:
        print(f"❌ Erro de entrada: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        

if __name__ == "__main__":
    main()