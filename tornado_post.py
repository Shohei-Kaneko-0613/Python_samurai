import tornado.ioloop
import tornado.web
import os
import json
import subprocess

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/tornado_post_html.html")
        
class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        post_data = self.get_argument("filename","test_post.py")
        #subprocess.call(["python", post_data])

        yaml_data = self.get_argument("","")
        path = yaml_data + post_data
        if os.path.exists(path):
            subprocess.call(["python", post_data])

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
