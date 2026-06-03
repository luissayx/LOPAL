mb = int(input("Digite um número em mb:"))
velo = int(input("Digite a velocidade do arquivo(Mbps):"))
formula = mb * 8
formula2 = formula / velo
print ("O tempo aproximado de dowload em segundo é de: ", formula2)
