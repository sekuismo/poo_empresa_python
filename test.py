import time
def cosaRara(numero):
    while True:
        time.sleep(0.05)
        if numero % 2 == 0:
            numero = numero / 2
            print(numero,'es  par ')
        else:
            numero = (numero * 3) + 1
            print(numero, ' es impar ')


cosaRara(9663)