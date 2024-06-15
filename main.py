from functools import reduce

numeros = [1, 2, 3, 4, 5]

listas_aninhadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def quadrado(x):
    return x ** 2

def somar(x, y):
    return x + y

def e_impar(x):
    return x % 2 != 0

def exibir_informacoes(lista):
    for i, num in enumerate(lista):
        print(f"Número {i+1}: {num}")

def achatar(lista):
    return [item for sublista in lista for item in sublista]

impares = list(filter(e_impar, numeros))
quadrados_impares = list(map(quadrado, impares))
print("Números ímpares:")
exibir_informacoes(impares)


print("\nQuadrados dos números ímpares:")
exibir_informacoes(quadrados_impares)


soma_dos_quadrados_impares = reduce(somar, quadrados_impares)
print("\nSoma dos quadrados dos números ímpares:", soma_dos_quadrados_impares)


lista_achatada = achatar(listas_aninhadas)
print("\nLista aninhada achatada:", lista_achatada)


soma_dos_quadrados_achatados = reduce(somar, map(quadrado, lista_achatada))
print("Soma dos quadrados da lista aninhada achatada:", soma_dos_quadrados_achatados)
