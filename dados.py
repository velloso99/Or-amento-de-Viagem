#Importadno o Sqlite3
import sqlite3 as lite

#Criando a conexao com o banco de dados
con = lite.connect('dados.db')

#Criando a tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Quantia(id INTEGER PRIMARY KEY AUTOINCREMENT, valor DECIMAL)")

#tabela de despesas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Despesas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, descricao TEXT, valor DECIMAL)")