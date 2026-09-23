import sqlite3

#conectando o banco de dados. Caso não existe, o banco é criado.

def cadastrar_usuario():
    conn = sqlite3.connect("biblioteca.db")

#Apaga a tabela usuarios
    conn.execute("DROP TABLE IF EXISTS usuarios")

#cria a tab usuarios
    conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")
    
#Inserindo os registros na tbela usuarios
    a = input("Digite o nome do usuario:")
    conn.execute("INSERT INTO usuarios(nome) VALUES(?)", [(a)])

#Confirmando a criação e os inserts da tabela usuarios
    conn.commit()


def listar_usuarios():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha[0]} | nome: {linha[1]}")

    conn.close()