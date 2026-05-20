nota1=int(input("Digite sua primeira nota: \n"))
nota2=int(input("Digite sua segunda nota: \n"))
nota3=int(input("Digite sua terceira nota: \n"))
media= (nota1 + nota2 + nota3) /3
print("Sua média é", media)
if media >= 7:
    print("Aprovado!")
elif media >= 5 and media < 7:
    print("Recuperação!")
else:
    print("Reprovado!")

