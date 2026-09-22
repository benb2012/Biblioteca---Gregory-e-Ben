import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela emprestimos
conn.execute("DROP TABLE IF EXISTS emprestimos")

#montando sql de criação de emprestimos
sql_create = """CREATE TABLE emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            usuario_id INTEGER REFERENCES usuarios(id), 
            data_emprestimo DATE DEFAULT CURRENT_DATE
          
            )"""

#cria a tabela 
conn.execute(sql_create)

##montando o sql do insert
sql_insert = """INSERT INTO emprestimos(usuario_id, data_emprestimo ) VALUES(?, ?)"""
 

#inserindo os registros na tabela 
conn.executemany(sql_insert, 
    [(1, '2026-09-08'), 
     (2, '2001-09-11')])

#confirmando a criação e os inserts da tabela 
conn.commit()