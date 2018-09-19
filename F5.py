import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/F5.html")

class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        self.write("OK")

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
