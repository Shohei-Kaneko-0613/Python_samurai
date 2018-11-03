import sqlite3

con = sqlite3.connect("test_data.db")
cur = con.cursor()

#sql1 = "create table fruits(name text, price text);"
#cur.execute(sql1)

#path=0

#テーブルの検索
#sql3 = "select * from fruits where name='test_post20.py'"
#cur.execute(sql3)
#for row in cur:
#    path=row[1]
#    print(path)



#テーブルの挿入
sql2 = "insert into fruits values('test_post20.py', '/Users/kanekoshohei/Documents/Git/Python/samurai/test_post20.py')"
cur.execute(sql2)
con.commit()
#sql = "delete from fruits where name='test_post20.py'"
#cur.execute(sql)
#con.commit()


con.close()
