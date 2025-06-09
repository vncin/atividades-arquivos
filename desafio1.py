while True:
    print("1 - Cadastrar produtos")
    print("2 - Listar produtos")
    print("3 - Buscar produtos")
    print("4 - Sair")
    op = int(input("Informe a opção: "))
    if op == 1:
        nome_prod = input("Informe o nome do produto: ")
        preco = float(input("Informe o preço do produto: "))
        with open("loja.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {nome_prod} | Preço: {preco}\n")
    elif op == 2:
        with open("loja.txt", "r", encoding="utf-8") as arquivo:
            produtos = arquivo.readlines()
            for produto in produtos:
                print(produto.strip())
    elif op == 3:
        busca = input("Informe o nome do produto que deseja buscar: ")
        encontrado = False
        with open("loja.txt", "r", encoding="utf-8") as arquivo:
            produtos = arquivo.readlines()
            for produto in produtos:
                produto.strip()
                nome, preco = produto.split("|")
                nome = nome.split(":")
                preco = preco.split(":")
                if nome[1].strip() == busca:
                    print(f"Nome: {nome[1]}| Preço: {preco[1]}")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado!")
    elif op == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
