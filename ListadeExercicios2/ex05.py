print("📚 Desconto em e-books")
livro = int(input("Digite o valor do seu livro:\n"))
if livro >80 :
    desconto = livro - (livro * 0.10)
    print("Você ganhou um desconto de 10%!, agora seu livro custa: ", desconto)
else:
    print("O valor do seu livro é de: ", livro)
