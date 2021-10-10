import sqlite3
db=sqlite3.connect('harendra.db')
cr=db.cursor()
cr.execute('create table login2(UNAME txt,UPASS TXT)')
db.commit()
db.close()
print("database crreated")