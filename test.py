import sqlite3

import sqlite3
conn = sqlite3.connect('test.db')

def create_table(): 
    c = conn.cursor()
    c.execute("CREATE TABLE person (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)")
    c.execute("insert into person values (1,'tinv')")
    c.execute("select * from person")
    c.execute("UPDATE person SET name = 'doanh vu' where id = 1")
    c.execute("insert into person values (2,'tinv')")
    c.execute("insert into person values (3,'lana')")
    c.execute("delete from person where id =3")
    conn.commit()
    conn.close()

def test():
    c = conn.cursor()
    c.execute('SELECT * FROM person')
    print(c.fetchall())
    conn.close()

if __name__ == "__main__":
    create_table()