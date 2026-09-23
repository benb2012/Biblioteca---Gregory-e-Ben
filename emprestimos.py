import datetime
import sqlite3
from conferir_id import verificar_id_existente

def cadastrar_emprestimos():
#conectando o banco de dados. Caso não exista, o banco é criado.    
    conn = sqlite3.connect("biblioteca.db")



#montando o sql do insert
    sql_insert = """INSERT INTO emprestimos(usuario_id, data_emprestimo ) VALUES(?, ?)"""
 

#inserindo os registros na tabela com a data formatada na hora que o usuário digitar

    data_emprestimo = input("Digite a data do empréstimo (DD/MM/AAAA) : ")
    usuario_id = int(input("Digite o ID do usuário: "))

#verificando se o id do usuário existe na tabela usuarios antes de inserir na tabela emprestimos
    if not verificar_id_existente("usuarios", usuario_id):
        print(f"Erro: O id {usuario_id} não existe na tabela usuarios.")
        return
    objeto_data = datetime.strptime(data_emprestimo, "%d/%m/%Y")
    conn.execute(sql_insert, (usuario_id, objeto_data.isoformat()))
#confirmando a criação e os inserts da tabela 
    conn.commit()






    


    

#listar os emprestimos 

def listar_emprestimos():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha[0]} | usuario_id: {linha[1]} | data_emprestimo: {linha[2]}")

    conn.close()