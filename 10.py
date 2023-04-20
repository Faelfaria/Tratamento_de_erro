while True :
    try:
        numero = int(input("Entre an int numero : "))
        print(5/numero)
        break
    except (VAlueError, ZeroDivisionError):
        print('Valor errado ou não é possível dividir por zero.')
    except: 
        print('DEsculpe, algo errado acontceu..')