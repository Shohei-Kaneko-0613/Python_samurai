import tornado.ioloop
import tornado.web
import requests
import os
import json
import subprocess

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/tornado_post_html.html")
        
class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
#        post_data = self.get_argument("filename","test_post.py")
        post_data = self.request.files["files_data"][0]["body"].decode()
        print(type(post_data),post_data)
        file="test.txt"
#        with open(file) as data1:
#            post_data2 = data1.read()
#        print(post_data2) 

#        data = subprocess.check_output(["cat", post_data])
        #print(data)

        DOWNLOAD_SAVE_DIR = "/Users/kanekoshohei/Documents/Git/Python/samurai/"
        saveFilePath = DOWNLOAD_SAVE_DIR + "test_post.py"
        #print(saveFilePath)
        with open(saveFilePath,mode="w") as saveFile:
            saveFile.write(post_data)
#            print(saveFile)
        subprocess.call(["python", saveFilePath])

def make_app():
    settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}
    return tornado.web.Application([
    (r"/", MainHandler),
    (r'/post_test/', MainHandler_post),
], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
