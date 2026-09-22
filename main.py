import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()

for linha in resultados:
    print(f"id: {linha[0]} | nome: {linha[1]}")

conn.close()