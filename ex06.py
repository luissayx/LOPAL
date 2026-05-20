usuario=input("Digite as credenciais fixas: \n")
senha=int(input("Digite a senha:\n"))
if usuario=="admin" and senha==1234:
    print("Login realizado com sucesso")
else:
    print("Credenciais inválidas")
