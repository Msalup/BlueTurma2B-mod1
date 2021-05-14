def IMC(peso, altura):
    #peso = 75
    #1altura = 1.68
IMC = peso /(altura**2)
print("O IMC é = {0:.2f}".format(IMC))

peso = float(input("Digite o peso do indivíduo[DIGITE UM VALOR NUMÉRICO] ")
altura = float(input("Digite o peso do indivíduo[DIGITE UM VALOR NUMÉRICO] ")


try:
    peso ´float(peso)
    altura = float(altura)
    IMC(peso, altura)
except:
    print("VOCÊ DIGITOU DADOS INVÁLIDOS")


"""peso = float(input("Digite o peso do indivíduo: ").replace(",", ".")).lower()).replace("Kg", "")).strip())
altura = float(input("Digite a altura do indivíduo: ").replace(",", ".")).lower()).replace("m", "")).strip())
IMC(peso, altura)"""
