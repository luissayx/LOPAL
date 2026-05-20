print("Validador de senha\n")
validas = ["senhaSegura66-", "PizzadeQueijo22@", "Peperonii2-"]
senha = ""
while senha != validas:
    senha = input("Digite sua senha: \n")
    if senha in validas:
        print("Acesso válido")
        break
    else:
        print("Senha inválida, necessita ter 8 caracteres:")



