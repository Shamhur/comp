import sqlite3

connection = sqlite3.connect("ds_1.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE data_time (time TEXT,temp TEXT);")
connection.commit()
connection.close()
