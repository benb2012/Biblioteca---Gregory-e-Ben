import sqlite3
from datetime import datetime
from conferir_id import verificar_id_existente

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")


def cadastrar_emprestimos_livros():

##montando o sql do insert
    sql_insert = """INSERT INTO emprestimos_livros(emprestimo_id, livro_id , data_devolucao ) VALUES(?, ?, ?)"""

#criando 

    id_emprestimo = int(input("Digite o ID do empréstimo: "))
    id_livro = int(input("Digite o ID do livro: "))
    data_string = input("Digite a data de devolução (DD/MM/AAAA) : ")

# confirmar se os id's existem nas tabelas emprestimos e livros antes de inserir na tabela emprestimos_livros
    if not verificar_id_existente("emprestimos", id_emprestimo):
        print(f"Erro: O id {id_emprestimo} não existe na tabela emprestimos.")
        return

    if not verificar_id_existente("livros", id_livro):
        print(f"Erro: O id {id_livro} não existe na tabela livros.")
        return

    objeto_data = datetime.strptime(data_string, "%d/%m/%Y")
    conn.execute(sql_insert, (id_emprestimo, id_livro, objeto_data.isoformat()))
    conn.commit()

   




    #confirmando a criação e os inserts da tabela editoras.
    conn.commit()

# listar os emprestimos cadastrados no banco de dados
def listar_emprestimos_livros():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos_livros")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"emprestimo_id: {linha[0]} | livro_id: {linha[1]} | data_devolucao: {linha[2]}")

    conn.close()