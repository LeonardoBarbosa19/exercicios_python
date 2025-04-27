# função que verifica se é uma palavra e polídromo
def eh_polídromo(palavra):
    palavra = palavra.lower(). replace(" ", "")
    return palavra == palavra [:: -1]

# função principal
def main():
    palavra = input ("digite uma palavra para verificar se ele é polídromo: ")

    if eh_polídromo(palavra):
       print(f" {palavra} é um polídromo.")
    else:
        print(f" {palavra} não é um polídromo.")

# execução do programa
if __name__ == "__main__":
    main()        