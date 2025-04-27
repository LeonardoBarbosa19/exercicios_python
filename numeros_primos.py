# função que verifica se um número primo
def eh_primo (n):
    if n <= 1:
        return False
    for i in range (2, int (n**0.5)+1):
        if n % i == 0:
            return False
    return True

# função principal
def main():
    try:
        numero = int (input("digite um número inteiro para verificar se é primo: "))
        if eh_primo(numero):
            print(f"o numero {numero} é primo")
        else:
            print(f"o numero {numero} não é primo")
    except ValueError:
        print("entrada inválida! por favor, digite um numero inteiro.")

# execução do programa
if __name__ == "__main__":
    main()                    

