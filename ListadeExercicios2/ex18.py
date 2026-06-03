print("Detector de Palíndromo:")
plvr = input("Digite uma palavra: ")
n = [*plvr]
contrario = ""
for i in range(1,len(n)+1):
    contrario = contrario + n [-i]
if contrario == plvr:
    print("Essa palavra é um políndromo")
else:
    print("Essa palavra não é um políndromo")
