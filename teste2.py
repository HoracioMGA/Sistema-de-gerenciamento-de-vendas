ids = []
produtos = []
quantidades = []
precos = []
totais = []
proximo_id = 1
pagamentos = []

def cadastrar_venda():
    global proximo_id
    print("CADASTRAR VENDA \n")
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preco unitario: "))
    total = quantidade * preco
    pagamento = input("Metodo de pagamento (pix, dinheiro, debito, credito): ")

    ids.append(proximo_id)
    produtos.append(produto)
    quantidades.append(quantidade)
    precos.append(preco)
    totais.append(total)
    pagamentos.append(pagamento)

    proximo_id = proximo_id + 1
    print("Venda cadastrada com sucesso! Total:", total)


def listar_vendas():
    print("LISTA DE VENDAS \n")
    if len(ids) == 0:
        print("Nenhuma venda cadastrada.")
        return

    soma_geral = 0
    for i in range(len(ids)):
        print(
            "ID:", ids[i],
            "| Produto:", produtos[i],
            "| Qtd:", quantidades[i],
            "| Preco:", precos[i],
            "| Total:", totais[i],
            "| Pagamento:", pagamentos[i]
        )
        soma_geral = soma_geral + totais[i]

    print("Total geral das vendas:", soma_geral)


def atualizar_venda():
    print("ATUALIZAR VENDA \n")
    id_procurado = int(input("Digite o ID da venda para atualizar: "))
    encontrou = False

    for i in range(len(ids)):
        if ids[i] == id_procurado:
            produtos[i] = input("Novo nome do produto: ")
            quantidades[i] = int(input("Nova quantidade: "))
            pagamentos[i] = input("Novo metodo de pagamento: ")
            precos[i] = float(input("Novo preco unitario: "))
            totais[i] = quantidades[i] * precos[i]
            print("Venda atualizada!")
            encontrou = True
            break

    if not encontrou:
        print("Venda nao encontrada.")


def excluir_venda():
    print("EXCLUIR VENDA \n")
    id_procurado = int(input("Digite o ID da venda para excluir: "))
    encontrou = False

    for i in range(len(ids)):
        if ids[i] == id_procurado:
            del ids[i]
            del produtos[i]
            del quantidades[i]
            del precos[i]
            del totais[i]
            del pagamentos[i]
            print("Venda excluida!")
            encontrou = True
            break

    if not encontrou:
        print("Venda nao encontrada.")


def main():
    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_venda()
        elif opcao == "2":
            listar_vendas()
        elif opcao == "3":
            atualizar_venda()
        elif opcao == "4":
            excluir_venda()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")


main()