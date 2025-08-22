'''
Considerando a a sequência numérica a seguir (11, 18, 25, 32, 39... ) 
Faça uma função que recebe como entrada uma posição e devolve qual o valor do número naquela posição,
considerando a sequência numérica apresentada, para todos os efeitos, a sequência começa da posição 1.

'''

def termo_sequencia(posicao: int) -> int:
    """
    A sequência apresentada no problema é uma progressão aritmética (PA):
    an = a1 + (n-1) * r
    onde: r é obtido pela diferença entre um número e o seu anterior imediato na sequência.
    Conhecendo a fórmula, não precisamos iterar ate a posição desejada. 
    """
    if posicao < 1:
        raise ValueError("A posição deve ser >= 1")
    return 11 + (posicao - 1) * 7


def main():
    try:
        n = int(input("Digite a posição desejada: "))
        print(f"O valor na posição {n} é {termo_sequencia(n)}")
        
    except ValueError:
         print("❌ Entrada inválida! Digite apenas um número inteiro maior ou igual a 1.")

if __name__ == "__main__":
    main()