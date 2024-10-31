numeros = [31, 40, 59, 26, 41, 58]

n = len(numeros)
for i in range(n):
    for j in range(0, n-i-1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print("Números em ordem crescente:")
for numero in numeros:
    print(numero)
