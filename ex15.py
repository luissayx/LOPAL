print("Cadastro múltiplo de usuários \n")
lista = []
for i in range(5):
    nome = input(f"Digite o nome do usuario {i+1} :\n")
    lista.append(nome)
print()
print("Nomes das pessoas da lista:\n")
for nome in lista:
    print (nome)


