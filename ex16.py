print("Controle de estoque:\n")
nomeprod = input("Digite o nome do produto: \n")
quantprod = int(input("Digite a quantidade de produto: \n"))
quantvend = int(input("Digite a quantidade vendida:\n"))
estoque = quantprod - quantvend
print("Nome: ", nomeprod)
print("A quantidade de estoque restante é: ", estoque )
if estoque <=0:
    print("Alerta")
