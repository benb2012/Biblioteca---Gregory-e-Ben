import sqlite3 as sqlite    
from autores import cadastrar_autores, listar_autores
from editoras import cadastrar_editoras, listar_editoras
from livros import cadastrar_livros, listar_livros
from usuarios import cadastrar_usuario, listar_usuarios
from emprestimos import cadastrar_emprestimos, listar_emprestimos
from emprestimos_livros import cadastrar_emprestimos_livros, listar_emprestimos_livros
from criar_tabelas import criar_tabelas
from usuarios import cadastrar_usuario, listar_usuarios


# criar um menu para o usuário escolher a opção desejada onde o usuário pode escolher entre cadastrar, listar ou sair do programa

while True:
    print("Escolha uma opção:")
    print("1 - Cadastrar editoras")
    print("2 - Listar editoras")
    print("3 - Cadastrar autores")
    print("4 - Listar autores")
    print("5 - Cadastrar livros")
    print("6 - Listar livros")
    print("7 - Cadastrar usuários")
    print("8 - Listar usuários")
    print("9 - Cadastrar empréstimos")
    print("10 - Listar empréstimos")
    print("11 - Cadastrar empréstimos de livros")
    print("12 - Listar empréstimos de livros")
    print("13 - Criar tabelas do banco de dados (Apagará todos os registros existentes)")
    print("0 - Sair")

    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        cadastrar_editoras()
    elif opcao == "2":
        listar_editoras()
    elif opcao == "3":
        cadastrar_autores()
    elif opcao == "4":
        listar_autores()
    elif opcao == "5":
        cadastrar_livros()
    elif opcao == "6":
        listar_livros()
    elif opcao == "7":
        cadastrar_usuario()
    elif opcao == "8":
        listar_usuarios()
    elif opcao == "9":
        cadastrar_emprestimos()
    elif opcao == "10":
        listar_emprestimos()
    elif opcao == "11":
        cadastrar_emprestimos_livros()
    elif opcao == "12":
        listar_emprestimos_livros()
    elif opcao == "13":
        criar_tabelas()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")



