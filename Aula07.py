
def aumento_salarial(salario = 5000, percentual=100):
    novo_salario = salario*percentual/100 + salario
    return novo_salario
"""salario_fulano = aumento_salarial()
print(salario_fulano)"""
def reducao_salarial(salario = 5000, percentual=10):
    novo_salario = salario - salario*percentual/100 
    return novo_salario
