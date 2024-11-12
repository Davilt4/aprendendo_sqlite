from pessoa import Pessoa
from sqlite import conectar, cadastrar_pessoa, listar_pessoas, criar_tabela,deletar_pessoa

if __name__ == "__main__":
    def menu_principal():
        print("1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Deletar Pessoa")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        return opcao

    conn = conectar()
    criar_tabela(conn)
    while True:
        opcao = menu_principal()
        if opcao == "1":
            nome = input("Digite o nome da pessoa: ")
            idade = input("Digite a idade da pessoa: ")
            pessoa = Pessoa(nome, idade)
            cadastrar_pessoa(conn, pessoa)
        elif opcao == "2":
            pessoas = listar_pessoas(conn)
            for pessoa in pessoas:
                print(f"ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}")
        
        elif opcao == "3":
            pessoa_id = input("Digite o ID da pessoa que deseja deletar: ")
            deletar_pessoa(conn, pessoa_id)
            
        elif opcao == "0":
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Programa encerrado.")