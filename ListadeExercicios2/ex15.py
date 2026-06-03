print("Contador de vogais")
frase = input("Digite uma frase:\n")
vogais = "aeiou"
vt = 0
for letras in frase:
    if letras in vogais:
        vt+= 1
print(f"Seu total de vogais é de : {vt}")
