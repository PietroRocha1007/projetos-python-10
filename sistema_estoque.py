import json

produtos = []


def salvar_produtos():
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)


def mostrar_menu():
    print("\n" + "=" * 50)
    print("             SISTEMA DE ESTOQUE")
    print("=" * 50)
    print("  [1]\tCadastrar produto")
    print("  [2]\tMostrar produtos")
    print("  [3]\tBuscar produto")
    print("  [4]\tAdicionar estoque")
    print("  [5]\tRetirar estoque")
    print("  [6]\tAtualizar preço")
    print("  [7]\tExcluir produto")
    print("  [8]\tRelatório de estoque")
    print("  [9]\tSair")
    print("-" * 50)


def carregar_produtos():
    global produtos

    try:
        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)

    except FileNotFoundError:
        produtos = []


def cadastrar_produto():
    produto_nome = input(">> Nome do produto: ").strip()

    if not produto_nome:
        print("! Nome do produto não pode estar vazio.")
        return

    for produto in produtos:
        if produto['nome'].lower() == produto_nome.lower():
            print("! Esse produto já está cadastrado.")
            return

    try:
        produto_preco = float(input(">> Preço do produto: R$ ").strip())

        if produto_preco <= 0:
            print("! O preço precisa ser maior que zero.")
            return

    except ValueError:
        print("! Digite um preço válido.")
        return

    try:
        produto_quantidade = int(input(">> Quantidade em estoque: ").strip())

        if produto_quantidade < 0:
            print("! A quantidade não pode ser negativa.")
            return

    except ValueError:
        print("! Digite uma quantidade inteira válida.")
        return

    produto = {
        "nome": produto_nome,
        "preco": produto_preco,
        "quantidade": produto_quantidade
    }

    produtos.append(produto)
    salvar_produtos()

    print("-" * 50)
    print(f"+ Produto '{produto_nome}' cadastrado com sucesso!")


def mostrar_produtos():
    print("\n--- PRODUTOS CADASTRADOS " + "-" * 26)

    if not produtos:
        print("  (Nenhum produto cadastrado.)")
        print("-" * 50)
        return

    for i, produto in enumerate(produtos, start=1):
        print(
            f"  {i:02} | Nome: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Quantidade: {produto['quantidade']}"
        )

    print("-" * 50)


def buscar_produto():
    if not produtos:
        print("  (Nenhum produto cadastrado.)")
        print("-" * 50)
        return

    buscar = input(">> Nome do produto a buscar: ").strip().lower()

    for produto in produtos:
        if produto['nome'].lower() == buscar:
            print(
                f"  Produto encontrado: Nome: {produto['nome']} | "
                f"Preço: R$ {produto['preco']:.2f} | "
                f"Quantidade: {produto['quantidade']}"
            )
            print("-" * 50)
            return

    print("! Produto não encontrado.")


def adicionar_estoque():
    if not produtos:
        print("  (Nenhum produto cadastrado.)")
        print("-" * 50)
        return

    buscar = input(">> Nome do produto para adicionar estoque: ").strip().lower()

    for produto in produtos:
        if produto['nome'].lower() == buscar:
            try:
                quantidade_adicionar = int(
                    input(">> Quantidade a adicionar: ").strip()
                )

                if quantidade_adicionar <= 0:
                    print("! A quantidade precisa ser maior que zero.")
                    return

            except ValueError:
                print("! Digite uma quantidade inteira válida.")
                return

            produto['quantidade'] += quantidade_adicionar
            salvar_produtos()

            print(
                f"+ Estoque atualizado. Nova quantidade de "
                f"'{produto['nome']}': {produto['quantidade']}"
            )
            return

    print("! Produto não encontrado.")


def retirar_estoque():
    if not produtos:
        print("  (Nenhum produto cadastrado.)")
        print("-" * 50)
        return

    buscar = input(">> Nome do produto para retirar estoque: ").strip().lower()

    for produto in produtos:
        if produto['nome'].lower() == buscar:
            try:
                quantidade_retirar = int(
                    input(">> Quantidade a retirar: ").strip()
                )

                if quantidade_retirar <= 0:
                    print("! A quantidade precisa ser maior que zero.")
                    return

            except ValueError:
                print("! Digite uma quantidade válida.")
                print("-" * 50)
                return

            if quantidade_retirar > produto['quantidade']:
                print(
                    f"! Quantidade insuficiente em estoque. "
                    f"Estoque atual de '{produto['nome']}': "
                    f"{produto['quantidade']}"
                )

            else:
                produto['quantidade'] -= quantidade_retirar
                salvar_produtos()

                print(
                    f"+ Estoque atualizado. Nova quantidade de "
                    f"'{produto['nome']}': {produto['quantidade']}"
                )

            print("-" * 50)
            return

    print("! Produto não encontrado.")


def atualizar_preco():
    if not produtos:
        print("  (Nenhum produto cadastrado.)")
        print("-" * 50)
        return

    buscar = input(">> Nome do produto para atualizar preço: ").strip().lower()

    for produto in produtos:
        if produto['nome'].lower() == buscar:
            try:
                novo_preco = float(
                    input(">> Novo preço do produto: R$ ").strip()
                )

                if novo_preco <= 0:
                    print("! O preço precisa ser maior que zero.")
                    return

                produto['preco'] = novo_preco
                salvar_produtos()

                print(
                    f"+ Preço atualizado. Novo preço de "
                    f"'{produto['nome']}': R$ {produto['preco']:.2f}"
                )
                print("-" * 50)
                return

            except ValueError:
                print("! Digite um preço válido.")
                print("-" * 50)
                return

    print("! Produto não encontrado.")


def excluir_produto():
    if not produtos:
        print("  (Nenhum produto cadastrado.)")
        print("-" * 50)
        return

    buscar = input(">> Nome do produto para excluir: ").strip().lower()

    for produto in produtos:
        if produto['nome'].lower() == buscar:
            confirmar = input(
                f"Tem certeza que deseja excluir '{produto['nome']}'? (s/n): "
            ).strip().lower()

            if confirmar != "s":
                print("Exclusão cancelada.")
                return

            produtos.remove(produto)
            salvar_produtos()

            print(f"+ Produto '{produto['nome']}' excluído com sucesso.")
            print("-" * 50)
            return

    print("! Produto não encontrado.")


def relatorio_estoque():
    if not produtos:
        print("  (Nenhum produto cadastrado.)")
        print("-" * 50)
        return

    print("\n--- RELATÓRIO DE ESTOQUE " + "-" * 26)

    for i, produto in enumerate(produtos, start=1):
        print(
            f"  {i:02} | Nome: {produto['nome']} | "
            f"Quantidade: {produto['quantidade']}"
        )

    print("-" * 50)


carregar_produtos()

while True:
    mostrar_menu()

    opcao = input(">> Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        mostrar_produtos()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        adicionar_estoque()

    elif opcao == "5":
        retirar_estoque()

    elif opcao == "6":
        atualizar_preco()

    elif opcao == "7":
        excluir_produto()

    elif opcao == "8":
        relatorio_estoque()

    elif opcao == "9":
        print("Saindo do sistema de estoque...")
        print("Até logo!")
        print("-" * 50)
        break

    else:
        print("! Opção inválida. Tente novamente.")
