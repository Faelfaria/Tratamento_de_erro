while True:
    try:
        numero = int(input('Entre com um número: '))
        print(5/numero)
        break
    except ValueError:
        print('Valor Errado.')
    except ZeroDivissionError:
        print('Desculpe.Não posso fazer isso por você.')
    except:
        print('Não sei o que fazer...')
        