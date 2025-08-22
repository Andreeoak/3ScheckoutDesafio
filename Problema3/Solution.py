'''
Um jogo com tabuleiro unidirecional comporta dois jogadores. Vence quem chegar primeiro a ultima casa do tabuleiro com menos turnos.

Para caminhar com as peças, os jogadores utilizam uma roleta que sorteia se devem andar 1, 2 ou 3 casas.

Caso tire um número maior na roleta, que casas faltantes, o jogador deve iniciar novamente o percurso (como um looping),

por exemplo, se faltam apenas duas casas para eu ganhar, e tiro 3 na roleta, devo caminhar as duas faltantes mais uma até a primeira casa do tabuleiro, reiniciando todo o percurso.

Regra: O tamanho mínimo do tabuleiro deve ser 3 casas sem um máximo.

Crie uma função que recebe o número de casas do tabuleiro e devolve:


1 - Quantidade mínimo de turnos para se chegar ao destino (caminho ótimo);
2 - Probabilidade de um usuário conseguir executar o caminho ótimo;
3 - Quantas combinações de movimentos diferentes um jogador conseguiria executar sem efetuar nenhum looping no tabuleiro.
'''


from collections import deque

def min_turns_tabuleiro(n: int) -> int:
    """
    Calcula o número mínimo de turnos para chegar à última casa (n-1)
    em um tabuleiro de n casas, seguindo as regras do jogo.
    
    Args:
        n: Número de casas no tabuleiro (n >= 3).
    
    Returns:
        O número mínimo de turnos para alcançar a casa n-1.
    """
    if not isinstance(n, int) or n < 3:
        raise ValueError("O tabuleiro deve ter no mínimo 3 casas e n deve ser um inteiro positivo")

    alvo = n - 1
    visitado = set([0])  
    fila = deque([(0, 0)])  # (posição, turnos)

    while fila:
        pos, turnos = fila.popleft()
        if pos == alvo:
            return turnos

        for passo in (1, 2, 3):
            prox = (pos + passo) % n
            if prox not in visitado:
                visitado.add(prox)
                fila.append((prox, turnos + 1))

    return -1  # fallback, nunca acontece para n >= 3

def count_optimal_paths(n: int) -> int:
    """
    Conta quantos caminhos distintos levam à vitória em exatamente min_turns.
    """
    min_turns = min_turns_tabuleiro(n)
    alvo = n - 1

    # dp[turno][pos] = quantidade de formas de chegar em pos com "turno" jogadas
    dp = [dict() for _ in range(min_turns + 1)]
    dp[0][0] = 1  # começa na posição 0

    for t in range(min_turns):
        for pos, count in dp[t].items():
            for passo in (1, 2, 3):
                prox = (pos + passo) % n
                dp[t + 1][prox] = dp[t + 1].get(prox, 0) + count

    return dp[min_turns].get(alvo, 0)


def prob_caminho_otimo(n: int) -> float:
    """
    Calcula a probabilidade de chegar ao destino pelo caminho ótimo.
    """
    min_turns = min_turns_tabuleiro(n)
    caminhos_otimos = count_optimal_paths(n)
    total_possiveis = 3 ** min_turns

    return caminhos_otimos / total_possiveis


def count_no_loop_paths(n: int) -> int:
    """
    Conta quantas combinações de movimentos diferentes um jogador pode fazer
    para chegar à última casa sem looping.
    
    Args:
        n: número de casas do tabuleiro (>= 3)
    
    Returns:
        Número de combinações possíveis sem looping.
    """
    if not isinstance(n, int) or n < 3:
        raise ValueError("O tabuleiro deve ter no mínimo 3 casas e n deve ser inteiro positivo")

    dp = [0] * (n)
    dp[0] = 1  # 1 jeito de estar na posição inicial

    for i in range(1, n):
        dp[i] = (dp[i-1] if i-1 >= 0 else 0) \
              + (dp[i-2] if i-2 >= 0 else 0) \
              + (dp[i-3] if i-3 >= 0 else 0)

    return dp[n-1]


def main():
    try:
        entrada = input("Digite o número de casas do tabuleiro (>= 3): ")
        n = int(entrada)

        # 1 - Mínimo de turnos
        min_turns = min_turns_tabuleiro(n)
        print(f"1) Mínimo de turnos para chegar à última casa: {min_turns}")

        # 2 - Probabilidade do caminho ótimo
        prob = prob_caminho_otimo(n)
        print(f"2) Probabilidade de executar o caminho ótimo: {prob:.6f} ({prob*100:.2f}%)")

        # 3 - Quantidade de caminhos sem looping
        no_loop_paths = count_no_loop_paths(n)
        print(f"3) Número de combinações de movimentos sem looping: {no_loop_paths}")

    except ValueError as e:
        print(f"❌ Erro: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()
