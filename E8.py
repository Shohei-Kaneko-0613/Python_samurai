import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/E8.html")

class MainHandler_post(tornado.web.RequestHandler):
    def post(self):
        number=int(self.get_argument('num1'))
        if number==1:
            self.render("static/E8-1.html")
        elif number==2:
            self.render("static/E8-2.html")
        elif number==3:
            self.render("static/E8-3.html")
        else:
            self.write("入力可能な数字は１〜３です。")


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
