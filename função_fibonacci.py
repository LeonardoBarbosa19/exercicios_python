# função que gera a sequencia de fibonacci
def fibonacci (n):
    sequencia = []
    a, b = 0, 1
    for _ in range (n):
        sequencia.append (a)
        a, b = b, a +b
        return sequencia
    
# função principal
def main ():
    try:
        n = int (input ("digite a quantidade de termos de sequencia de fibonacci que deseja ve"))
        if n <= 0:
            print ("por favor, digite um numero inteiro positivo.")
        else:
            resultado = fibonacci (n)
            print ("sequencia de fibonacci com ", n, "termos: ")
            print (resultado)
    except ValueError:
        print ("entrada invalida! por favor, digite um numero inteiro.")

# execução do programa
if __name__ == "__main__":
    main ()
                    