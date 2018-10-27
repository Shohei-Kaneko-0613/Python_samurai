import tornado.ioloop
import tornado.web
import requests
import os
import json
import subprocess

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../static/tornado_post_html.html")

#ファイルの有無を確認し、ファイルがあればファイルパスをレスポンスする        
class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        first_post = self.get_argument("files_data2")
        print(first_post)
        result = subprocess.check_output(["find" , "/Users/kanekoshohei/Documents/Git/Python/samurai" , "-name", first_post])
        print(result)
        print(type(result))
        print(len(result))
        if 1 <= len(result): 
            self.write(result)
        else:
            self.write("")

#MainHandler_postでファイル有無の判定で有りの場合、ファイルの実行を行う
class MainHandler_post2(tornado.web.RequestHandler):
    def post(self):
        
        second_post = self.get_argument("files_data3")
        print(second_post)
        subprocess.call(["python",second_post])
        
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
        


def make_app():
    settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}
    return tornado.web.Application([
    (r"/", MainHandler),
    (r'/post_test/', MainHandler_post),
    (r'/post_test2/', MainHandler_post2),
    (r'/post_test3/', MainHandler_post3),
], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
