    


import sqlite3


def criar_tabelas():

    print(" ATENÇÃO: Ao confirmar essa opção você apagara todas as tabelas do banco de dados e PERDERA TODOS os registros, \n" \
    " para assim recriar as tabelas VAZIAS e SEM os dados,\n " \
    "apenas faça em caso de erros graves ou da falta de um banco de dados criado.\n Deseja continuar? (S/N)")

    opcao = input("Digite S para continuar ou N para cancelar: ")

    if opcao.upper() == "S":
        print(" Apagando e criando as tabelas do banco de dados...")
    elif opcao.upper() == "N":
        print(" Cancelando a operação...")
        return
    else:
        print(" Opção inválida. Cancelando a operação...")
        return

    #conectando o banco de dados. Caso não exista, o banco é criado.
    conn = sqlite3.connect("biblioteca.db")

    #criando editoras
    
    #Apaga a tabela editoras caso ela exista
    conn.execute("DROP TABLE IF EXISTS editoras")

    #cria a tab editoras com os campos id e nome
    conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

    #criando autores
    

        #Apaga a tabela autores caso ela exista
    conn.execute("DROP TABLE IF EXISTS autores")

        #cria a tab autores com os campos id e nome
    conn.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")


    #criando livros

        #apaga a tabela livros
    conn.execute("DROP TABLE IF EXISTS livros")

        #montando sql de criação de livros
    sql_create = """CREATE TABLE livros (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT NOT NULL, autor_id INTEGER REFERENCES autores(id), 
            editora_id INTEGER REFERENCES editoras(id),
            ano_publicacao INTEGER,
            edicao INTEGER,
            disponivel BOOLEAN NOT NULL DEFAULT 1 CHECK (disponivel IN(0,1))
            )"""

        #cria a tabela editoras
    conn.execute(sql_create)

    #criando usuarios

    #criando emprestimos
    
    

        #apaga a tabela emprestimos
    conn.execute("DROP TABLE IF EXISTS emprestimos")

        #montando sql de criação de emprestimos
    sql_create = """CREATE TABLE emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            usuario_id INTEGER REFERENCES usuarios(id), 
            data_emprestimo DATE DEFAULT CURRENT_DATE

          
            )"""

        #cria a tabela 
    conn.execute(sql_create)

    #criando emprestimos_livros

        #apaga a tabela caso ela exista
    conn.execute("DROP TABLE IF EXISTS emprestimos_livros")

        #montando sql de criação da tabela emprestimos_livros
    sql_create = """CREATE TABLE emprestimos_livros (emprestimo_id INTEGER references emprestimos(id), 
            livro_id INTEGER REFERENCES dados_livros(id), 
            data_devolucao date default CURRENT_DATE,
            PRIMARY KEY (emprestimo_id, livro_id)
          
            )"""

        #cria a tabela 
    conn.execute(sql_create)