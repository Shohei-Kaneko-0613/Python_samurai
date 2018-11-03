import tornado.ioloop
import tornado.web
import requests
import os
import json
import subprocess
import tornado.httpserver
import sqlite3

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../static/tornado_post_html.html")
        
#ファイルの有無を確認し、ファイルがあればファイルパスをレスポンスする        
class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        first_post = self.get_argument("files_data2")
        
#DB検索
        path=""
        con = sqlite3.connect("test_data.db")
        cur = con.cursor()
        sql3 = "select * from fruits where name='test_post20.py'"
        cur.execute(sql3)
        for row in cur:
            path=row[1]
            print(path)
        con.close()


#select文で検索ヒットすればTrue            
        if 1 <= len(path): 
            self.write("file search OK")
#select文で検索ヒットしなければFalse,DBにカラム追加
        else:
            self.write("")
            con = sqlite3.connect("test_data.db")
            cur = con.cursor()
            sql2 = "insert into fruits values('test_post20.py', '/Users/kanekoshohei/Documents/Git/Python/samurai/test_post20.py')"
            cur.execute(sql2)
            con.commit()
            con.close()

#MainHandler_postでファイル有無の判定で有りの場合、ファイルの実行を行う
class MainHandler_post2(tornado.web.RequestHandler):
    def post(self):
        second_post = self.get_argument("files_data3")
        DB_file = "test_data.db"
        connection = sqlite3.connect(DB_file)
        cur = connection.cursor()
        sql3 = "select * from fruits where name='test_post20.py'"
        cur.execute(sql3)
        for row in cur:
            path=row[1]        
        subprocess.call(["python",path])
        
#MainHandler_postの判定でファイルが無ければ、ファイルを作成して実行する
class MainHandler_post3(tornado.web.RequestHandler):
    def post(self):
        
        post_data = self.request.files["files_data"][0]["body"].decode()


        DOWNLOAD_SAVE_DIR = "/Users/kanekoshohei/Documents/Git/Python/samurai/"
        saveFilePath = DOWNLOAD_SAVE_DIR + "test_post20.py"
        #print(saveFilePath)
        with open(saveFilePath,mode="w") as saveFile:
            saveFile.write(post_data)
            print(saveFile)
        subprocess.call(["python", saveFilePath])
        


make_app=tornado.web.Application([
    (r"/", MainHandler),
    (r'/post_test/', MainHandler_post),
    (r'/post_test2/', MainHandler_post2),
    (r'/post_test3/', MainHandler_post3),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(make_app, ssl_options={
        "certfile":"server.crt",
        "keyfile":"server.key",
    })
    http_server.listen(8443)
tornado.ioloop.IOLoop.current().start()
