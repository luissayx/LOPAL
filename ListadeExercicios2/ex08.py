print("⚖️ Calculadora de IMC (Índice de Massa Corporal)")
peso, altura= float(input("Digite o seu peso(em Kg):\n")), float(input("Digite sua altura(em metros):\n"))
imc = peso / altura ** 2
print("Seu Imc é de",  imc)
