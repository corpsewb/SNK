def main():
    nome  = input ("Digite seu nome: ")
    quantIrmaos = int (input ("DIgite quantos irmaos vc tem "))
    altura = float (input("DIgite a sua altura: "))
    isCabelo = input ("vc tem cabelo? ")

    print("0 ", nome, "  tem", quantIrmaos,"e", altura, "de altura" )
 
    if isCabelo == "SIM" or isCabelo == "s":
        print("Ele possui cabelo ")
    else:
        print("Ele nao possui cabelo")
    return 0
main()
