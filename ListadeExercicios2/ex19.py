print("Validador de portas de rede")
while True:
    porta = int(input("Digite uma porta: "))
    if porta == 80 or porta == 443:
        print("Porta Liberada")
        break
    else:
        print("Porta bloqueada, tente outra")
