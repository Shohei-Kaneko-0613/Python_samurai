import sqlite3

con = sqlite3.connect("test_data.db")
con.execute("create table t1 (col1 int)")
con.commit()
con.execute("insert into t1 values(10)")
con.commit()
file = con.execute("select * from t1")
for _C in file:
    print(_C)
