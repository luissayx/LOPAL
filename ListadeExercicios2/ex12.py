resultado = 1
n = int(input("Digite um número inteiro:\n"))
for i in range (n,0, -1):
    resultado *=i
print(f"Fatorial de {n} é {resultado}")
