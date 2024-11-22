import sqlite3

conn = sqlite3.connect('data/database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE students ( name text, age integer, gender text, marjor text)')
print("Created table successfully!.....")

conn.close()