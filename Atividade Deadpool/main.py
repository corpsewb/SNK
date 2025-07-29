def main():

    idade = int (input("Qual a sua idade "))
    if idade >= 18:
        print ("entrada autorizada")
    elif idade <= 16:
        acompanhante = input ("algum responsavel presente ")
        if acompanhante == "sim": 
            print ("entrada autorizada")

        else:
            print ("nao autorizada") 
    else:
        print ("entrada proibida")
    return 0
main()