from produto import Produto
from dados import conectar, cadastrar_produto, listar_produtos, criar_tabela, deletar_produto

if __name__ == "__main__":
    def menu_principal():
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Deletar Produto")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        return opcao
    
    conn = conectar()
    criar_tabela(conn)
    while True:
        opcao = menu_principal()
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = input("Digite o preço do produto: ")
            validade = input("Digite a validade do produto: ")
            fabricante = input("Digite o fabricante do produto: ")
            descricao = input("Digite a descrição do produto: ")
            produto = Produto(nome, preco, validade,fabricante,descricao)
            cadastrar_produto(conn, produto)
        elif opcao == "2":
            produtos = listar_produtos(conn)
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Validade: {produto[3]}, Fabricante: {produto[4]}, Descrição: {produto[5]}")
        elif opcao == "3":
            produto_id = input("Digite o ID do produto que deseja deletar: ")
            deletar_produto(conn, produto_id)
        elif opcao == "0":
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Programa encerrado.")


