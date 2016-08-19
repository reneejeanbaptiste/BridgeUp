import sqlite3
conn = sqlite3.connect('PythonSql.db')
c.execute('''CREATE TABLE stocks
             ('Student'text, 'Dorm' text, Student Id text, qty real, price real)''')

