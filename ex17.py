
prod1 = int (input("Digite o preço do primeiro produto:\n"))
prod2 = int (input("Digite o preço do segundo produto: \n"))
prod3 = int (input("Digite o preço do terceiro produto:\n"))
prod4 = int (input("Digite o preço do quarto produto:\n"))
prod5 = int (input("Digite o preço do quinto produto:\n"))
subtotal = prod1 + prod2 + prod3 + prod4 + prod5
print("O seu subtotal é ", subtotal)
imposto = subtotal + (subtotal*0.1)
print("O seu valor final com o imposto é de: ", imposto)
