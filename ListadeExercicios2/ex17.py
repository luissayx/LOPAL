print("Urna eletrônica:\nAlice=1 \nBob= 2")
alice = 0
bob = 0
while True:
    v= int(input("Digite o número do seu eleitor:\n"))
    if v == 1:
        alice += 1
    elif v == 2:
        bob += 1
    elif v == 0:
        break
print(f"Alice possui {alice} votos, e bob {bob} votos ")
