import sqlite3
from datetime import datetime
#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela livros
conn.execute("DROP TABLE IF EXISTS emprestimos_livros")

#montando sql de criação de livros
sql_create = """CREATE TABLE emprestimos_livros (emprestimo_id INTEGER references emprestimos(id), 
            livro_id INTEGER REFERENCES dados_livros(id), 
            data_devolucao DATE
          
            )"""

#cria a tabela 
conn.execute(sql_create)

##montando o sql do insert
sql_insert = """INSERT INTO emprestimos_livros(emprestimo_id, livro_id , data_devolucao ) VALUES(?, ?, ?)"""

#criando data

data_string = "12/09/2026"
objeto_data = datetime.strptime(data_string, "%d/%m/%Y")
conn.execute(sql_insert, (1, 1, objeto_data.isoformat()))
conn.commit()

data_string = "11/09/2002"
objeto_data = datetime.strptime(data_string, "%d/%m/%Y")
conn.execute(sql_insert, (2, 2, objeto_data.isoformat()))
conn.commit() 

#inserindo os registros na tabela editoras
# conn.executemany(sql_insert, 
#     [(1, 1, '2027-09-08'), 
#      (2, 2, '2002-09-11')])


#confirmando a criação e os inserts da tabela editoras.
conn.commit()