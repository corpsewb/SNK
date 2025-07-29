import random
def mein ():
    numeroAleatorio = random.randint(0, 10)

    numero = -1 
    i = 0 
    while numeroAleatorio != numero:

        numero = int (input ("Digite um numero "))

        if numero > numeroAleatorio:
            print ("O seu numero é maior")
        elif numero < numeroAleatorio:
            print ("O seu numero é menor")

        i += 1 
    print ("voce acertou com ", i, "tentativas")        

    return 0 
mein ()