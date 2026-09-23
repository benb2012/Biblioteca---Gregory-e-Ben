import sqlite3

def cadastrar_editoras():
    #conectando o banco de dados. Caso não existe, o banco é criado.
    conn = sqlite3.connect("biblioteca.db")



    #Inserindo os registros na tbela editoras
    ed = input("Digite o nome da editora:")
    conn.execute("INSERT INTO editoras(nome) VALUES(?)", [(ed)])

    #Confirmando a criação e os inserts da tabela editoras
    conn.commit()

def listar_editoras():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM editoras")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha[0]} | nome: {linha[1]}")

    conn.close()