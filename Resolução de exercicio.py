"""list = [5, 7, 2, 9, 4, 1, 3]

print(len(list))

maior_valor = max(list)
print(maior_valor)

menor_valor = min(list)
print(menor_valor )

soma_valor = sum(list)
print(soma_valor)

list.sort()
print(list)

list.reverse()
print(list)
"""
"""
def conta_vogal(frase):
    vogais = 0
    for letra in frase:
        if letra.upper() in "AEIOU":
            vogais += 1
    return vogais
    
frase_str = input("Digite uma palavra ou frase para contarmos as vogais: ")
print("A palavra/frase",frase_str,"possui",conta_vogal(frase_str),"vogais")"""


def some_vogal(frase):
    vogais = "aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûüÍÌÎíìî"
    for letra in vogais:
        if letra in frase:
            frase = frase.replace(letra,"")
    return frase

str_frase = input("Digite uma palavra ou frase para retirarmos as vogais: ")
#print(str_frase)
print("A palavra ou frase que você digitou: '",str_frase.upper(), "'retiradas as vogais ficam segintes :", some_vogal(str_frase).upper())
