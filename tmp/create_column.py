import sqlite3

con = sqlite3.connect("test_data.db")
cur = con.cursor()



#テーブルの挿入
sql2 = "insert into fruits values('test_post20.py', '/Users/kanekoshohei/Documents/Git/Python/samurai/test_post20.py')"
cur.execute(sql2)
con.commit()


con.close()
