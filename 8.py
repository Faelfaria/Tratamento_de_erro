while True:
    try:
        numero = int(input('Entre com um numero: '))
        print(numero/2)
        break
    except:
        print('O numero que você entrou não é válido, tente novamente.')