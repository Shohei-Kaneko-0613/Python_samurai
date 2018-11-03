import sqlite3

con = sqlite3.connect("test_data.db")
cur = con.cursor()

sql = "delete from fruits where name='test_post20.py'"
cur.execute(sql)
con.commit()


con.close()
