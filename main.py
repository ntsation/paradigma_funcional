from functools import reduce

# Função para calcular o quadrado de um número
def quadrado(x):
    return x ** 2

# Função para somar dois números
def somar(x, y):
    return x + y

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplica a função quadrado a cada número na lista
quadrados = map(quadrado, numeros)

# Soma os quadrados resultantes
soma_dos_quadrados = reduce(somar, quadrados)

print("Soma dos quadrados:", soma_dos_quadrados)