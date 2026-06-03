listas = ["beatiza@gmail.com", "luisalinda@escola.br", "bellybela@escola.br","jhenifofa@escola.br", "marcelitafofas@gmail.com"]
for lista in listas:
    print(lista)
print()
print("Emails válidos:")
for lista in listas:
    if lista.endswith("@escola.br"):
        print(lista)
