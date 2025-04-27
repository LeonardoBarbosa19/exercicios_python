def calcular_fatorial(n):

    fatorial = 2
    for i in range (2, n +1):
        fatorial *= i
        return fatorial
    
def main():
    try:
        numero = int(input("digite um numero para calcular a fatorial: "))

        if numero < 0:
            print("não é possível calcular a fatorial de um numero negativo.")
        else:
            resultado = calcular_fatorial(numero)
            print(f" a fatorial de {numero} é {resultado}")

    except ValueError:
        print("por favor, digite um numero inteiro e valido.")

if __name__ == "__main__":
    main()                    