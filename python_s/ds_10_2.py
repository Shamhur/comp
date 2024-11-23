import sqlite3

connection = sqlite3.connect("ds_1.sl3", 5 )
cur = connection.cursor()
cur.execute("INSERT INTO data_time (time, temp) VALUES ('14:30', '0')")
connection.commit()
cur.execute("SELECT rowid, temp FROM data_time;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()




