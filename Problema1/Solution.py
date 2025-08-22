'''
Escreva uma função que determina se uma string termina com 'A' e começa com 'B'
'''

def string_comeca_com_B_e_termina_com_A(texto: str) -> bool: 
    '''
    Interpretando o enunciado literalmente, procuramos pelas letras 'A' maiúscula no final e 'B' maiúscula no começo,
    embora faça mais sentido procurarmos por 'a' minúsculo no final.
    '''   
    return texto.startswith("B") and texto.endswith("A") # O(1) em Python. So checa o primeira e o ultimo posicao 


def main():
    entrada = input("Digite uma string: ")
    if string_comeca_com_B_e_termina_com_A(entrada):
        print("✅ A string começa com 'B' e termina com 'A'.")
    else:
        print("❌ A string não atende aos critérios.")


if __name__ == "__main__":
    main()
    
