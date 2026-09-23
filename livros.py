import sqlite3
from conferir_id import verificar_id_existente

def cadastrar_livros():
    conn = sqlite3.connect("biblioteca.db")


#montando o sql do insert
    sql_insert = """INSERT INTO livros(titulo, autor_id, editora_id, ano_publicacao, edicao,
    disponivel) VALUES(?, ?, ?, ?, ?, ?)"""
 

#inserindo os registros na tabela editoras
    titulo = input("Digite o título do livro: ")
    autor_id = int(input("Digite o ID do autor: "))
    editora_id = int(input("Digite o ID da editora: "))
    ano_publicacao = int(input("Digite o ano de publicação: "))
    edicao = int(input("Digite a edição: "))
    disponivel = int(input("Digite se o livro está disponível (1 para sim, 0 para não): "))

    #verifica se o autor_id existe na tabela autores
    if not verificar_id_existente("autores", autor_id):
        print(f"Erro: O autor_id {autor_id} não existe na tabela autores.")
        return
    if not verificar_id_existente("editoras", editora_id):
        print(f"Erro: O editora_id {editora_id} não existe na tabela editoras.")
        return
    else:
        print("IDs válidos. Prosseguindo com o cadastro do livro.")


    conn.execute(sql_insert, 
    (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel))

#confirmando a criação e os inserts da tabela editoras.
    conn.commit()


def listar_livros():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha[0]} | titulo: {linha[1]} | autor_id: {linha[2]} | editora_id: {linha[3]} | ano_publicacao: {linha[4]} | edicao: {linha[5]}")

    conn.close()