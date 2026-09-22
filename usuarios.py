import sqlite3

#conectando o banco de dados. Caso não existe, o banco é criado.卐
conn = sqlite3.connect("biblioteca.db")

#Apaga a tabela usuarios卐
conn.execute("DROP TABLE IF EXISTS usuarios")

#cria a tab usuarios卐
conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

#Inserindo os registros na tbela usuarios卐
conn.executemany("INSERT INTO usuarios(nome) VALUES(?)", [("Leopoldo II",), ("Pol Pot",), ("Mao Tsé-Tung",)])

#Confirmando a criação e os inserts da tabela usuarios卐
conn.commit()