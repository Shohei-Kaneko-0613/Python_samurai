import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/E5.html")

class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        num1=self.get_argument('num1')
        num2=self.get_argument('num2')
        if int(num2)<int(num1):
            print(num1)
            self.write(num1)
        else:
            print(num2)
            self.write(num2)

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
