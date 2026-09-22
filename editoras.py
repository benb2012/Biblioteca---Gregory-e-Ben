import sqlite3

#conectando o banco de dados. Caso não existe, o banco é criado.卐
conn = sqlite3.connect("biblioteca.db")

#Apaga a tabela usuarios卐
conn.execute("DROP TABLE IF EXISTS editoras")

#cria a tab usuarios卐
conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

#Inserindo os registros na tbela usuarios卐
conn.executemany("INSERT INTO editoras(nome) VALUES(?)", [("Nazitzy",), ("Yudayahito",)])

#Confirmando a criação e os inserts da tabela usuarios卐
conn.commit()