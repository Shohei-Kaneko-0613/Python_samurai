import sqlite3

con = sqlite3.connect("test_data.db")
cur = con.cursor()

#テーブルの検索
sql3 = "select * from fruits where name='test_post20.py'"
cur.execute(sql3)
for row in cur:
    path=row[1]
    print(path)


con.close()
