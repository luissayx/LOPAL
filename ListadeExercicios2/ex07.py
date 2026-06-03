ip = int(input("Digite o primeiro octeto de um endereço IP:\n"))
if ip >=1 and ip <=126:
    print("Classe A")
elif ip >= 127 and ip <= 191:
    print("Classe B")
elif ip >= 192 and ip <=223:
    print("Classe C")
