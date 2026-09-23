import sqlite3


def cadastrar_autores():
#conectando o banco de dados. Caso não existe, o banco é criado.
    conn = sqlite3.connect("biblioteca.db")


#Inserindo os registros na tbela autores

    aut = input("Digite o nome do autor:")

    conn.executemany("INSERT INTO autores(nome) VALUES(?)", [(aut)])

#Confirmando a criação e os inserts da tabela autores
    conn.commit()


#lista os autores cadastrados no banco de dados
def listar_autores():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha[0]} | nome: {linha[1]}")

    conn.close()