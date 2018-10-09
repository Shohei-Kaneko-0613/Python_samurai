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
#        with open(data2,"r") as data1:
#            post_data2 = data1.write(data2)
        

#        data = subprocess.check_output(["cat", post_data])
#        print(post_data2)

#        DOWNLOAD_SAVE_DIR = "/Users/kanekoshohei/Documents/Git/Python/samurai/"
#        saveFilePath = os.path.join(DOWNLOAD_SAVE_DIR, "test_post.py")
#        with open(saveFilePath,"wb") as saveFile:
#            saveFile.write(post_data)
#        print(saveFile)
#        subprocess.call(["sh", saveFile])

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
