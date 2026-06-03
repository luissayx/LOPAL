print("💰 Reajuste de bolsa auxílio")
bolsa = int(input("Digite  o valor atual da sua bolsa de estagiário:\n"))
if bolsa <= 1000:
    aumento = (bolsa * 0.15) + bolsa
    print("Você recebeu um aumento de 15% agora seu valor é de" , aumento)
else:
    aumento2 = (bolsa * 0.10)+ bolsa
    print("Você recebeu um aumento de 10% agora seu valor é de", aumento2)
