with open("dados.txt", "r") as arquivo:
    info = arquivo.read()

with open("novos_dados.txt", "w") as novo_arq:
    novo_arq.write(info)
    