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
        post_data = self.get_argument("filename","test_post.py")
#        data = subprocess.check_output(["cat", post_data])
#        print(data)
#        data2 = requests.get(post_data)
        with open(post_data) as data1:
            post_data2 = data1.read()
        

        data = subprocess.check_output(["cat", post_data])
        #print(data)

        DOWNLOAD_SAVE_DIR = "/Users/kanekoshohei/Documents/Git/Python/samurai/"
        saveFilePath = DOWNLOAD_SAVE_DIR + "test_post.py"
        #print(saveFilePath)
        with open(saveFilePath,"wb") as saveFile:
            saveFile.write(data)
        #print(saveFile)
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
