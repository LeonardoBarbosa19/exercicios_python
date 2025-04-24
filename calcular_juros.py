# função que calcule o montante de juros compostos
def calcular_juros(capital, taxa, tempo):
    montante = capital * (1 + taxa) ** tempo
    return montante

# função principal
def main ():
    try:
        capital = float (input ("digite o valor inicial (capital) em R$"))
        taxa = float (input("digite o valor em taxas de juros mensal em (%)"))
        tempo = float (input("digite o tempo em meses"))

        # convertendo taxa em percentual para decimal
        taxa_decimal = taxa / 100

        montante = calcular_juros (capital, taxa_decimal, tempo)

        print (f"montante após {tempo} meses: R$ {montante : .2f}")
    except ValueError:
        print ("entrada invalida! certifique-se de digitar números validos.")   

# execução do programa
if __name__== "__main__":
    main ()        