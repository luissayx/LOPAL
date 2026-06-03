print("🏫 Monitoramento de presença")
faltas = float(input("Digite seu percentual de faltas acumuladas:\n"))
if faltas >=12.5:
    print("Atenção: Limite de ausência atingido")
else:
    print("Frequência regular")
