with open("frases.txt", "w", encoding="utf-8") as frases:
    frases.write("Hoje o dia está bonito\n")
    frases.write("Vou estudar Python\n")
    frases.write("Arquivos são legais de usar\n")

with open("frases.txt", "r") as arquivo:
    lista_frases = arquivo.readlines()
    contagem = 0
    arq_final = open("contagem.txt", "a")
    for n_linha, frase in enumerate(lista_frases):
        contagem = len(frase.strip().split())
        arq_final.write(f"Linha {n_linha+1}: {contagem}\n")
    arq_final.close()
print("Fim do arquivo!")