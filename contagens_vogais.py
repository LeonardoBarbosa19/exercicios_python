# função que solicita uma palavra vogal e exiba
def contar_vogais (palavra):
    vogais = "aeiou ou AEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

# função principal
def main ():
    palavra = input ("digite uma palavra")
    total_vogais = contar_vogais (palavra)
    print(f"A palavra '{palavra}' contém {total_vogais} vogal(is).")

# execução do programa
if __name__ == "__main__":
         main()    