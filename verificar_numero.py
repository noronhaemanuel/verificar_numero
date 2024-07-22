def verificar_numero():
    try:
        # Dizer se um número é positivo ou negativo
        número = float(input("Insira um número: "))

        if número > 0:
            print ("Número positivo")
        elif número < 0:
            print("Número negativo")
        else:
            print("Valor nulo")   
    except ValueError:
        print("Digite valor valido")
verificar_numero()