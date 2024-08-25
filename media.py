def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

def main():
    print("Bem-vindo ao calculador de média!")
    numeros = []
    
    while True:
        entrada = input("Digite um número (ou 'sair' para finalizar): ")
        
        if entrada.lower() == 'sair':
            break
        
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")
    
    media = calcular_media(numeros)
    print(f"A média dos números digitados é: {media:.2f}")

if __name__ == "__main__":
    main()
