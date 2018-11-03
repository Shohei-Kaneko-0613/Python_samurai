import tornado.ioloop
import tornado.web
import os
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/F1_js.html")
        

def make_app():
    settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}
    return tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
